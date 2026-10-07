# Django Weblog Project

A weblog application built with Django that enables publishing and managing blog posts through a clean and organized web interface.

This project was developed as a learning project to practice Django development, template rendering, static file management, media uploads, and database-driven web applications.

## Features

- Blog post management
- Dynamic content rendering with Django Templates
- Media file uploads (images)
- Static asset management (CSS, JavaScript, Images)
- Django Admin integration
- SQLite database
- Modular Django application structure

## Technology Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

## Project Structure

```text
Django_weblog_project/
│
├── media/
│   └── images/
│
├── myblog/                 # Project configuration
│
├── posts/                  # Blog application
│   ├── migrations/
│   ├── templatetags/
│   └── ...
│
├── static/
│   └── assets/
│       ├── css/
│       ├── js/
│       └── img/
│
├── templates/
│   └── blogs/
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/amyr36/Django_weblog_project.git
cd Django_weblog_project
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Create an Admin User

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Static and Media Files

### Static Files

Project static resources are located in:

```text
static/assets/
```

Including:

- CSS stylesheets
- JavaScript files
- Images and UI assets

### Media Files

Uploaded images are stored in:

```text
media/images/
```

## Django Apps

### Posts

The main application responsible for:

- Managing blog content
- Rendering blog pages
- Handling templates
- Custom template tags

## Learning Objectives

This project was created to gain hands-on experience with:

- Django MVC (MVT) architecture
- Template inheritance
- Static and media file handling
- Database migrations
- Django Admin
- URL routing
- Application organization and modular design

## Future Improvements

- User authentication
- Comment system
- Categories and tags
- Search functionality
- Pagination
- Rich text editor
- REST API with Django REST Framework
- PostgreSQL support
- Docker deployment

## Author

**Amir Hossein Hamidi**

GitHub: https://github.com/amyr36

## License

This project is available for educational and personal learning purposes.
