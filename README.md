<p align="center">
  <img src="banner.png" alt="Django Blog Banner" width="100%">
</p>

<h1 align="center"> Django Blog — Dark Pro Theme </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Django-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Made with Django">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT">
  <img src="https://img.shields.io/badge/Maintained-Yes-success?style=for-the-badge" alt="Maintained">
</p>

<p align="center">
A professional, dark-themed Django blog project featuring modern design, interactive UI, and rich editing experience.
</p>

---

## ✨ Features

- 🎨 **Tailwind Dark UI** with animated cards & smooth transitions  
- 📝 **Summernote Rich Text Editor** (supports YouTube/Vimeo embeds)  
- 💬 **Moderated Comments** system with approval workflow  
- 🎬 **YouTube video preview fallback** (fixes Error 153 embed issue)  
- 📄 **Pagination & responsive layouts**  
- ⚙️ Built using Django Class-Based Views (ListView + DetailView)

---

## ⚡ Quickstart

```bash
# 1️⃣ Create & activate a virtual environment
python -m venv venv
source venv/Scripts/activate   # On Windows Git Bash

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run migrations
python manage.py migrate

# 4️⃣ Start the development server
python manage.py runserver


mysite/
│
├── blog/
│   ├── templates/blog/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── post_detail.html
│   │   └── sidebar.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── LICENSE
└── README.md
