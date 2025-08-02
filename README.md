# Moovy - Video Rental Website

Moovy is a Django-based web application for renting movies online. It features user authentication (login/logout), a movie catalog, and a user profile page.

---

## Features

- User registration, login, logout  
- Movie browsing  
- User profile page  
- Clean Bootstrap 5 based UI
- Admin features - add/remove/edit movies

---

## Technologies Used

- Python 3.12  
- Django 2.1  
- Bootstrap 5  
- SQLite (default Django database)  

---

## Installation and Setup

1. Clone the repository

```bash
git clone https://github.com/vihangarasanjali/moovy.git
cd moovy
```
2.Create and activate a virtual environment
```
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
3.Apply migrations
```
python manage.py migrate
```
4.Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```
5. Run the development server
```
python manage.py runserver
```





