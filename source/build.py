#!/usr/bin/env python3
"""Build dependency-free static HTML site from Jinja2 content and templates."""
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from content import PROFILE, CASE_STUDIES, CAPABILITIES, PRINCIPLES

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'public'
TEMPLATES = Path(__file__).resolve().parent / 'templates'
ENV = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=select_autoescape(['html']))

def render(template, destination, **context):
    destination.parent.mkdir(parents=True, exist_ok=True)
    output = ENV.get_template(template).render(profile=PROFILE, **context)
    destination.write_text(output, encoding='utf-8')
    print('wrote', destination.relative_to(ROOT))

render('home.html', SITE / 'index.html', root='', body_class='home', page_title='Subhash | Principal / Lead Data Platform Architect', description='Subhash is a hands-on Azure Data Platform Architect and Engineer with 15+ years in enterprise technology, governed lakehouses, platform engineering and production AI workflows.', case_studies=CASE_STUDIES, capabilities=CAPABILITIES, principles=PRINCIPLES)
for index, case in enumerate(CASE_STUDIES):
    next_case = CASE_STUDIES[(index + 1) % len(CASE_STUDIES)]
    render('case.html', SITE / 'work' / f"{case['slug']}.html", root='../', body_class='case-page', page_title=f"{case['title']} | Subhash", description=case['short'], case=case, next_case=next_case)

(SITE / 'robots.txt').write_text('User-agent: *\nAllow: /\n', encoding='utf-8')
