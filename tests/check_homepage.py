"""Dependency-free checks for the static homepage. Run: python3 tests/check_homepage.py"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
class CheckHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []; self.ids = []; self.links = []; self.assets = []; self.headings = []; self.papers = 0
    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == 'html': assert attrs.get('lang') == 'en'
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag == 'a':
            assert 'a' not in self.stack, 'Nested link'
            assert attrs.get('href'), 'Empty link'
            self.links.append(attrs['href'])
        if tag == 'li': assert self.stack[-1] in {'ol', 'ul'}, 'List item without list'
        if tag == 'img':
            assert 'alt' in attrs, 'Image without alt text'
            self.assets.append(attrs['src'])
        if tag in {'h1', 'h2', 'h3'}: self.headings.append(tag)
        if 'publication' in attrs.get('class', '').split(): self.papers += 1
        if tag not in VOID: self.stack.append(tag)
    def handle_startendtag(self, tag, pairs):
        self.handle_starttag(tag, pairs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'Mismatched closing {tag}, stack {self.stack}'
        self.stack.pop()

source = (ROOT / 'index.html').read_text()
assert source.lower().startswith('<!doctype html>')
p = CheckHTML(); p.feed(source); p.close()
assert not p.stack, p.stack
assert not [key for key, count in Counter(p.ids).items() if count > 1], 'Duplicate IDs'
assert p.headings.count('h1') == 1
assert p.papers >= 14
local = 0
for url in p.links + p.assets:
    if url.startswith('#'):
        assert unquote(url[1:]) in p.ids, f'Broken anchor {url}'
    elif not urlsplit(url).scheme:
        assert (ROOT / unquote(urlsplit(url).path)).is_file(), f'Missing local file {url}'
        local += 1
assert 'prefers-reduced-motion: reduce' in source
assert 'id="experience"' in source and 'href="#experience"' in source
assert 'Worked on integrating reinforcement learning (RL) updates into the ERNIE Thinking model.' in source
assert 'skip-link' in source and 'aria-live="polite"' in source
assert '<meta charset="utf-8">' in source
assert 'name="viewport"' in source and 'name="description"' in source
assert 'rel="canonical"' in source
print(f'PASS: HTML nesting, unique IDs, one h1, {p.papers} publications, {local} local file references, anchors, SEO, and accessibility hooks.')
print('This is a static check. Browser layout, contrast, and assistive-technology behavior require browser QA.')

assert 'menglinghui2019@ia.ac.cn' not in source
assert source.count('mailto:mengreinhold@163.com') == 2
assert '>mengreinhold@163.com</a>' in source
print('PASS: both active email links and displayed contact use mengreinhold@163.com.')
