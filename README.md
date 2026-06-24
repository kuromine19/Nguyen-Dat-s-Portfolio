# 🌐 Personal Portfolio — Mine Rua

A full-stack personal portfolio website built with Django, showcasing skills, projects, certifications, and blog posts.

**Live:** <In-progress>

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
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | HTML, CSS, Bootstrap 5 |
| Static files | WhiteNoise |
| Deployment | AWS EC2 (Ubuntu 22.04) |
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


## 📬 Contact

- Email: nguyendat19222002@gmail.com
- GitHub: https://github.com/kuromine19
- LinkedIn: https://www.linkedin.com/in/nguyendat19/
