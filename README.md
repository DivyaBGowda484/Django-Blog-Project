# 📝 VibeBoard – A Django Blog Platform

VibeBoard is a simple, elegant backend focused blogging platform built with Django. It allows users to publish blog posts, manage content through an admin panel, and view all posts on a clean homepage.

---

## 🚀 Live Demo

🌐 [Live on Render](https://vibeboard-o3qg.onrender.com)

---

## 📌 Features

- 📝 Create, update, and delete blog posts
- 📋 Post pagination for easy browsing
- 💬 Commenting system for blog readers
- 🛠️ Django admin interface for post
- 📱 Responsive UI using Django templates
- 🗃️ SQLite support for local development
- 🐘 PostgreSQL support for production (via Render)

---

## 🧱 Tech Stack

- **Backend:** Django 5.2
- **Database (Local):** SQLite3
- **Database (Production):** PostgreSQL via Render
- **Frontend:** HTML, CSS, Django Templates
- **Deployment:** Render

---

## ⚙️ Project Setup (Local)

### 1. Clone the repo
```bash
git clone https://github.com/DivyaBGowda484/VibeBoard.git
cd VibeBoard
```

### 2. Create & activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Apply migrations:
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

