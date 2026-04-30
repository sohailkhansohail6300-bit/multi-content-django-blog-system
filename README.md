# Django Multi-Category Blog System

## Project Overview

This is a full-stack Django-based multi-category blog platform designed to manage and publish different types of content including Documentaries, Stories, Food articles, Travel blogs, and News posts.

The system supports complete user authentication, profile management, CRUD operations, commenting system, search functionality, pagination, and a personalized user dashboard.

This project demonstrates strong backend development skills using Django, including ORM relationships, dynamic routing, modular architecture, and real-world web application design patterns.

---

## Key Features

### Content Management System

* Multi-category content structure:

  * Documentaries
  * Stories
  * Food Articles
  * Travel Blogs
  * News Posts
* Full CRUD functionality (Create, Read, Update, Delete)
* Image upload support for posts
* Latest-first content ordering using timestamps

---

### User Authentication System

* User registration and login system
* Secure authentication using Django built-in auth
* Profile system with image and bio support
* User-specific dashboard for managing posts
* Logout functionality

---

### Comment System

* Dynamic commenting system for all content types
* Each comment is linked to specific content via relational mapping
* User-based comment tracking
* Timestamped comments with ordering
* AJAX-style JSON response for submissions

---

### Search System

* Global search across all categories
* Case-insensitive filtering using Django ORM
* Real-time filtering of content by title

---

### Pagination System

* Pagination implemented for all listing pages
* 6 items per page for optimized performance
* Efficient handling of large datasets

---

## Tech Stack

* Backend: Django (Python)
* Database: SQLite
* Frontend: HTML, Tailwind CSS
* ORM: Django ORM
* Authentication: Django built-in authentication system
* Media Handling: Django ImageField
* Architecture: Django MVT (Model View Template)

---

## Project Architecture

```
project-root/
│
├── blog/                 # Core content application
│   ├── models.py
│   ├── views.py
│
├── accounts/             # Authentication & user management
│   ├── models.py
│   ├── views.py
│
├── templates/            # HTML templates
├── static/               # CSS and frontend assets
├── media/                # Uploaded images
├── db.sqlite3            # Database (development)
└── manage.py
```

---

## Database Design

### Content Models

All content models follow a consistent structure:

* title
* category
* image
* description
* created_at
* User_relation (ForeignKey to User)

Models:

* Documentry
* Story
* Food
* Travel
* News

---

### Comment Model

The comment system supports multiple content types using relational fields:

* d_relation (Documentry)
* s_relation (Story)
* f_relation (Food)
* t_relation (Travel)
* n_relation (News)
* content
* created_at
* User_relation (ForeignKey to User)

---

### Profile Model

* One-to-One relationship with Django User model
* Profile image upload
* Bio field for user description
* Account creation timestamp

---

## Application Flow

### Home Page

* Displays latest posts from all categories
* Search functionality integrated
* Quick preview of recent content

### Detail Page

* Full content view
* Related posts section
* Comment system per post

### Category Pages

* Dedicated pages for each content type
* Pagination enabled for performance

### User Dashboard

* View user-created posts
* Edit and delete posts
* Manage all personal content

---

## Authentication Flow

* User signup with validation checks
* Login system with authentication backend
* Profile update functionality
* Secure session-based login/logout system

---

## Key Technical Implementation

* Django ORM for database operations
* ForeignKey relationships for relational mapping
* Dynamic routing for category-based content
* Class-based model architecture
* Conditional query filtering using `icontains`
* Form handling with POST requests
* File upload handling for images

---

## Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/your-username/repository-name.git
cd /core/
```


---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## Admin Panel Access

```
http://127.0.0.1:8000/admin/
```

Admin Features:

* Manage users
* Manage posts
* Manage comments
* Manage profiles

---

## Skills Demonstrated

* Django backend development
* MVC/MVT architecture understanding
* ORM-based database design
* Authentication and authorization system
* File upload handling
* Dynamic routing and query filtering
* Relational database design
* CRUD system implementation
* Scalable Django project structure

---

## Project Summary

This project demonstrates a production-style Django application with real-world features including authentication, relational database design, dynamic content management, and scalable architecture. It is suitable for junior backend developer roles and portfolio presentation.

---

## Author

Muhammad Sohail
Django Developer

---


* Or help you **deploy this project live (PythonAnywhere / Render)**

