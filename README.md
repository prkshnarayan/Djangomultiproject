# Django Multi-Project

A Django project containing two applications:
1. Sales Management System
2. Music Player

This is a simple sales management and Musicplayer project built using the 
Django Framework, Python, HTML, CSS, MySQL Database, and JavaScript.
With this project, we can perform CRUD operations (CREATE, READ, UPDATE, and DELETE) 
in sales management project and manage songs from admin panel in musia player .
✓Task: Sales Management
✓Editor: Pycharm (Django Framework)
To access the application login and authentication is reguired.

## Technologies Used
- Django Framework
- Python
- HTML, CSS, JavaScript (Frontend)
- MySQL Database
- Bootstrap (for responsive design)

## Features

### Sales Management System
- Full CRUD operations (Create, Read, Update, Delete)
- Has both sales page and admin page (Admin has access to manage all the data and the sales person data)
- Customer management
- Sales tracking
- Admin dashboard

### Music Player
- Add/Manage songs through admin panel
- Play, pause, skip tracks
- Create and manage playlists
- User-friendly interface

## Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/prkshnarayan/Djangomultiproject.git
   cd Djangomultiproject
Steps to download manually:
1. Download the repository
2. Install Python(Django) (pip install django)
3. Activate your environment (envname Scripts activate)
   run the following commands:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser (This user can access the admin panel)
   python manage.py createuser (Admin panel is not accessed)
   (login with both user and superuser to compare the difference between the type of users)
   (Admin (superuser) has all the access, where as user has a limited access)
5. Run the server (python manage.py runserver)
