# 📝 ThinkNote

ThinkNote is a simple, secure, and theme-friendly note-taking web app built with Flask. It supports user authentication, note creation, deletion, and light/dark mode. The project is structured in a scalable and modular way, following Flask best practices.

---

## 📦 Features

- ✅ User Signup/Login/Logout
- 🗒️ Create and delete personal notes
- 🌗 Dark/Light mode with toggle
- 💾 Data stored using SQLite
- ⚙️ Flash message feedback
- 🎨 Responsive UI with Bootstrap

---

## 🧰 Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Database:** SQLite
- **Templating:** Jinja2

---

## 📂 Project Structure (Explained)

This app follows the **Blueprint and App Factory** pattern — making it modular and scalable.

### Root Directory (`FlaskProject/`)

| File/Folder       | Description |
|-------------------|-------------|
| `main.py`         | Entry point for the app. It imports and runs `create_app()` from the `website` package. |
| `database.db`     | SQLite database file auto-created when the app first runs. Stores users and notes. |
| `requirements.txt`| Lists all required Python libraries like Flask and SQLAlchemy. Used for setting up the environment. |

---

### `website/` — Application Package

| File/Folder        | Description |
|--------------------|-------------|
| `__init__.py`      | Initializes Flask app, configures it, registers Blueprints, and sets up the database. |
| `models.py`        | Contains database models for `User` and `Note`. Defines their structure and relationships. |
| `auth.py`          | Contains authentication routes: signup, login, logout. |
| `views.py`         | Contains routes for home page and handling notes (add/delete). |
| `static/`          | Holds static files like JavaScript, CSS, images. Includes: |
| → `index.js`       | Handles client-side actions like note deletion and dark mode toggle. |
| → `favicon.ico`    | Custom icon shown in the browser tab. |
| `templates/`       | Holds all HTML templates rendered by Flask using Jinja2. Includes: |
| → `base.html`      | Base layout with navbar, theme toggle, flash messages. Used by other pages. |
| → `login.html`     | Form for users to log in. |
| → `sign_up.html`   | Form for users to sign up. |
| → `home.html`      | Main notes page where users can add and delete notes. |

---

