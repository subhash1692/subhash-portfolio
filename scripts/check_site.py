#!/usr/bin/env python3
"""Check local static links referenced by public HTML pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

PUBLIC = Path(__file__).resolve().parent.parent / "public"

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for field in ('href', 'src'):
            if a.get(field):
                self.links.append(a[field])
        if tag == 'meta' and a.get('property') == 'og:image' and a.get('content'):
            self.links.append(a['content'])

errors = []
html_files = sorted(PUBLIC.rglob('*.html'))
if len(html_files) < 5:
    errors.append('Expected homepage plus four case studies')
for page in html_files:
    parser = Links()
    parser.feed(page.read_text(encoding='utf-8'))
    for url in parser.links:
        u = urlsplit(url)
        if u.scheme or u.netloc or url.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
            continue
        target = (page.parent / unquote(u.path)).resolve() if u.path else page
        if not target.is_relative_to(PUBLIC.resolve()):
            errors.append(f'{page.relative_to(PUBLIC)}: unsafe path {url}')
        elif not target.exists():
            errors.append(f'{page.relative_to(PUBLIC)}: missing {url}')
        elif u.fragment and target.suffix == '.html':
            page_text = target.read_text(encoding='utf-8')
            if f'id="{u.fragment}"' not in page_text and f"id='{u.fragment}'" not in page_text:
                errors.append(f'{page.relative_to(PUBLIC)}: missing fragment {url}')

for must in ['index.html', 'styles.css', 'script.js', 'assets/favicon.svg', 'assets/og-cover.png', 'assets/Subhash_Data_Platform_Architect_Resume.pdf']:
    if not (PUBLIC / must).is_file():
        errors.append(f'Missing required file: {must}')

if errors:
    print('Site validation failed:')
    for error in errors:
        print(' -', error)
    raise SystemExit(1)
print(f'Site validation passed: {len(html_files)} HTML pages and local links checked.')
