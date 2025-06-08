# Django Authentication Project

This is a Django-based web application that includes user authentication features such as registration, login, logout, profile dashboard, and styled alerts using SweetAlert2 and Bootstrap.

## 🚀 Features

- User Registration & Login
- Profile Dashboard
- Bootstrap 5 Styling
- SweetAlert2 Notifications
- CSRF Protection
- Modular Template Inheritance

---

## 🛠️ Requirements

- Python 3.8+
- pip (Python package manager)
- virtualenv (optional but recommended)

---

## ⚙️ Setup Instructions (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

Activate the environment:

- On Windows:
  ```bash
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist yet, you can create it:
```bash
pip freeze > requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (for Admin Access)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 📁 Project Structure

```
your_project/
├── manage.py
├── your_app/
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── base.html
│   │   │   └── login.html
│   │   └── register.html
│   ├── views.py
│   ├── models.py
│   └── ...
├── static/
│   └── styles.css
├── db.sqlite3
└── requirements.txt
```

---

## ✅ Tech Stack

- Django 5.x
- Bootstrap 5.1
- SweetAlert2
- SQLite (Default DB)

---

## 📦 Static Files Setup

Ensure this is in your `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

---

## 🧪 Testing the App

- Try registering a new user
- Log in with valid credentials
- Modify profile and see alert popups
- Access Django admin at `/admin/`

---