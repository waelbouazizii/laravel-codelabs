#!/usr/bin/env python3
"""Validate the generated codelab pages in docs/.

Checks every docs/*.html file for three things:

  1. Emoji characters anywhere in the file (forbidden by CLAUDE.md).
  2. Anchor links (href="#...") whose target id does not exist in the same
     file — i.e. a sidebar/step link pointing nowhere.
  3. A literal "..." inside a <code> block, which means the code sample is
     incomplete instead of the full, runnable snippet CLAUDE.md requires.
     A comment line ending with "..." is allowed (literal file content).

No third-party dependencies: only the Python 3 standard library is used.

Exit code: 0 if every file passes, 1 if any file has a problem.
"""

import glob
import os
import re
import sys
from html.parser import HTMLParser

# Emoji ranges called out in CLAUDE.md: misc symbols/pictographs + emoticons
# (U+1F300-U+1FAFF) and the older "misc symbols" / dingbats block
# (U+2600-U+27BF) that also carries common emoji such as checkmarks, stars,
# and weather symbols.
EMOJI_PATTERN = re.compile("[\U0001F300-\U0001FAFF☀-➿]")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")


def is_literal_comment_ellipsis(code_line):
    """True when '...' ends the line and sits inside a comment.

    CLAUDE.md (Copy blocks): file content shown for reading is reproduced
    literally, including comments that end with "...".
    """
    stripped = code_line.strip()
    if not stripped.endswith("..."):
        return False
    if stripped.startswith(("//", "#", "*", "/*")):
        return True
    return " // " in code_line[:code_line.rfind("...")]


class PageChecker(HTMLParser):
    """Collects ids, internal '#...' links, and <code> block text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.hash_links = []  # list of (target_id, line_number)
        self._code_depth = 0
        self._code_line_stack = []
        self._code_text_stack = []
        self.code_issues = []  # list of (line_number, snippet)

    def _register_common(self, tag, attrs):
        attrs_dict = dict(attrs)
        el_id = attrs_dict.get("id")
        if el_id:
            self.ids.add(el_id)
        if tag == "a":
            href = attrs_dict.get("href", "")
            if href.startswith("#") and len(href) > 1:
                self.hash_links.append((href[1:], self.getpos()[0]))
        if tag == "code":
            self._code_depth += 1
            self._code_line_stack.append(self.getpos()[0])
            self._code_text_stack.append([])

    def handle_starttag(self, tag, attrs):
        self._register_common(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        # Self-closing tag: still may carry an id/href, never opens <code>.
        attrs_dict = dict(attrs)
        el_id = attrs_dict.get("id")
        if el_id:
            self.ids.add(el_id)
        if tag == "a":
            href = attrs_dict.get("href", "")
            if href.startswith("#") and len(href) > 1:
                self.hash_links.append((href[1:], self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag == "code" and self._code_depth > 0:
            self._code_depth -= 1
            line = self._code_line_stack.pop()
            text = "".join(self._code_text_stack.pop())
            for offset, code_line in enumerate(text.split("\n")):
                if "..." in code_line and not is_literal_comment_ellipsis(code_line):
                    snippet = " ".join(code_line.strip().split())[:80]
                    self.code_issues.append((line + offset, snippet))

    def handle_data(self, data):
        if self._code_depth > 0:
            self._code_text_stack[-1].append(data)


def check_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    problems = []

    # 1. Emoji scan, line by line for a useful line number.
    for lineno, line in enumerate(content.splitlines(), start=1):
        for match in EMOJI_PATTERN.finditer(line):
            ch = match.group()
            problems.append(
                "line %d: forbidden emoji character %r (U+%04X)"
                % (lineno, ch, ord(ch))
            )

    # 2 & 3. Parse the markup for ids, internal links, and code blocks.
    parser = PageChecker()
    try:
        parser.feed(content)
        parser.close()
    except Exception as exc:  # malformed markup should not crash the check
        problems.append("HTML parse error: %s" % exc)
        return problems

    for target, lineno in parser.hash_links:
        if target not in parser.ids:
            problems.append(
                'line %d: link to "#%s" has no matching id="%s" in this file'
                % (lineno, target, target)
            )

    for lineno, snippet in parser.code_issues:
        problems.append(
            'line %d: incomplete code block contains "...": %r' % (lineno, snippet)
        )

    return problems


def main():
    files = sorted(glob.glob(os.path.join(DOCS_DIR, "*.html")))

    print("Codelab site check")
    print("=" * 60)

    if not files:
        print("No HTML files found in docs/ - nothing to check.")
        print("=" * 60)
        print("RESULT: PASS (nothing to check)")
        return 0

    all_ok = True
    for path in files:
        rel = os.path.relpath(path, REPO_ROOT)
        problems = check_file(path)
        if problems:
            all_ok = False
            print("[FAIL] %s (%d issue(s))" % (rel, len(problems)))
            for p in problems:
                print("    - %s" % p)
        else:
            print("[PASS] %s" % rel)

    print("=" * 60)
    if all_ok:
        print("RESULT: PASS - all files clean")
        return 0
    else:
        print("RESULT: FAIL - fix the issues above")
        return 1


if __name__ == "__main__":
    sys.exit(main())
