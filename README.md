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
- OpenAI

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

## AI Chatbot Integration

Moovy includes an AI-powered chatbot to assist users with movie recommendations and general queries.

### Features
- Ask about movie suggestions, genres, and availability.
- Interactive chat interface built with Django and Bootstrap.
- Chatbot powered by OpenAI's GPT models (`gpt-3.5-turbo` or `gpt-4o-mini`).

### Setup
1. **Add your OpenAI API key** in a `.env` file at the project root:






