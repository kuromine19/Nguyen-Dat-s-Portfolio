# 🌐 Personal Portfolio — Nguyen Dat
A full-stack personal portfolio website built with Django, showcasing skills, projects, certifications, and blog posts.

**Live:** https://nguyendatsportfolio.site

---

## 📸 Preview

| Home | Dashboard | Blog |
|------|-----------|------|
| Hero section with CTA | Skills, Projects, Certs | Articles & tutorials |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap 5 |
| Static files | WhiteNoise |
| Deployment | Render (Gunicorn) |
| DNS / CDN | Cloudflare |
| Version control | Git, GitHub |

---

## 📁 Project Structure

```
portfolio/
├── core/                        # Main app
│   ├── templates/
│   │   ├── base/
│   │   │   └── base.html        # Base template, navbar
│   │   └── core/
│   │       ├── home.html        # Landing page
│   │       ├── dashboard.html   # Skills, Projects, Certs
│   │       ├── about.html       # About me + timeline
│   │       ├── blog.html        # Blog listing
│   │       └── contact.html     # Contact form
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── portfolio/                   # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                      # CSS, JS, images
├── build.sh                     # Render build script
├── render.yaml                  # Render service definition
├── requirements.txt
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Pages

- **Home** — Hero section, tech stack tags, CTA buttons
- **Dashboard** — Technical & professional skills with animated bars, projects grid, certifications list
- **About** — Bio, contact links, experience timeline
- **Blog** — Article listing with category filters
- **Contact** — Contact form with email, location, social links

---

## 🚀 Run locally

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## ☁️ Deployment (Render)

1. On [Render](https://render.com), choose **New → Blueprint** and connect this repository. Render reads `render.yaml`, runs `build.sh` and starts Gunicorn.
2. Every push to the deployed branch redeploys automatically.
3. Custom domain: in the service's **Settings → Custom Domains** add `nguyendatsportfolio.site` and `www.nguyendatsportfolio.site`, then create the DNS records Render shows in Cloudflare.

Environment variables (set by `render.yaml`): `DJANGO_SECRET_KEY` (generated), `DJANGO_DEBUG=False`. Optional: `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS` (comma-separated).

## 📬 Contact

- Email: nguyendat19222002@gmail.com
- GitHub: https://github.com/kuromine19
- LinkedIn: https://www.linkedin.com/in/nguyendat19/
