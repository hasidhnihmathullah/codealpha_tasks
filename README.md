# codealpha_tasks

# CodeAlpha Internship - Task 1: E-Commerce Web Application

This repository contains the completed submission for Task 1 of the CodeAlpha Web Development Internship.



📌 Project Overview
A full-stack, responsive e-commerce platform built with Django. It features product catalog browsing, category filtering, cart management, user authentication, and product data initialization.

---

 Tech Stack
* Backend: Python, Django
* Database: SQLite
* Frontend: HTML5, CSS3, JavaScript

Key Features
* Dynamic product listing with category filtering
* Interactive shopping cart functionality
* Automated initial database seeding (`setup_data.py`)
* Django admin dashboard for managing inventory and orders



 Intern Details
* Name: Hasidh Nihmathullah
* Domain: Web Development
* Batch: September Batch

📂 Project Structure

```text
codealpha_tasks/
│
├── config/                 # Core Django project settings, WSGI, and URL routing
├── store/                  # Store application (models, views, forms, urls)
├── static/                 # Static assets (stylesheets, JavaScript, product media)
│   └── images/products/    # Product catalog images
├── templates/              # HTML templates (storefront, cart, checkout, base)
├── manage.py               # Django management command utility
├── setup_data.py           # Automated database seeding script
├── db.sqlite3              # Local SQLite database
└── README.md               # Project documentation
