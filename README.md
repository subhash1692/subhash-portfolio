# Subhash | Principal / Lead Data Platform Architect

A static, responsive professional portfolio featuring four sanitized engineering case studies, an architecture-first introduction, and a public resume. This is a personal, noncommercial job-search portfolio.

## Hosting

Built to deploy on Vercel from GitHub without a build step or paid domain.

1. Create a GitHub repo called `subhash-portfolio` under your own account.
2. Add the contents of this folder to the repository root (the `public/` folder must remain a folder).
3. Open https://vercel.com/new and import `subhash-portfolio` from your connected GitHub account.
4. Vercel settings: Framework Preset **Other**, project Root Directory **./**, output **public**, and **no build command**. The included `vercel.json` sets the framework and output folder.
5. Deploy. Vercel will assign a `.vercel.app` URL, which can then be shared on the resume and LinkedIn.

Every subsequent push to the default branch triggers a new production deployment if Git integration remains enabled.

## Structure

- `public/` - committed deployable HTML, CSS, JavaScript, public resume PDF and images.
- `source/content.py` - editable professional profile and case studies.
- `source/templates/` - Jinja2 source templates.
- `source/build.py` - local static page generator.
- `vercel.json` - Vercel framework and output directory settings.
- `scripts/check_site.py` - validates internal links and required static files.
- `.github/workflows/verify.yml` - basic GitHub pull-request checks.

## Updating site content

Use Python 3.10+ and install local authoring dependencies:

```bash
python -m pip install -r requirements-dev.txt
python source/build.py
python scripts/check_site.py
```

The generated pages are committed under `public/`; no Python or dynamic application runtime is needed on Vercel. Existing CSS and JavaScript can be edited directly in `public/`.

## Content and privacy

The case studies describe generalized engineering approaches and intentionally exclude internal customer resource names, client credentials, nonpublic diagrams, and proprietary source code. Public-site impact figures should be added only after verifying them. The downloadable public resume does not publish a personal phone number. The contact email in the source is `subhash1692@gmail.com`.

Before using this as a consulting services site or other commercial deployment, check Vercel plan terms: its free Hobby tier is for personal, noncommercial use only.