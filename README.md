# Inventory Management API

A Django REST API for tracking and managing assets.
---
## Login
![image](https://github.com/user-attachments/assets/917e3c5c-7338-4a30-9a2f-409033a79da3)
---
## Admin page
![image](https://github.com/user-attachments/assets/fcd80758-8a2e-40e4-ae1f-9a5aa877a8e3)
---
## Add Group (showing **assets**)
![image](https://github.com/user-attachments/assets/9d89a2d1-8e42-4728-8097-c9f67559087e)
---
## Add Group (showing **users**)
![image](https://github.com/user-attachments/assets/3c27a9af-993f-48f7-a94d-b032b74b692a)

## Features

- JWT authentication
- Custom user model with roles (admin, manager, viewer)
- Asset management with status tracking
- DRF and drf-spectacular for API schema/docs

## Setup

### 1. Clone the repository

```sh
git clone [inventory-api](https://github.com/afzalhussein/inventory-api)
cd inventory-api
```

### 2. Create and activate a virtual environment

```sh
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Install PostgreSQL and create the database

- Ensure PostgreSQL is running.
- Create a database named `inventory_db`:

```sh
psql -U postgres
CREATE DATABASE inventory_db;
\q
```

### 5. Configure settings (if needed)

Edit `config/settings.py` for your database credentials if needed.

### 6. Run migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser

```sh
python manage.py createsuperuser
```

### 8. Run the development server

```sh
python manage.py runserver
```

### 9. Run tests

```sh
pytest
```

## Requirements

Add the following to your `requirements.txt`:

```
Django>=5.2,<6.0
djangorestframework
drf-spectacular
djangorestframework-simplejwt
django-filter
psycopg2-binary
pytest
pytest-django
```

## API Endpoints

- **Assets:** `/api/assets/`
- **Authentication:** `/api/token/`, `/api/token/refresh/`
- **API Docs:** `/api/schema/`, `/api/docs/`

## Notes

- Make sure `django-filter` is installed:  
  `pip install django-filter`
- If you use pytest, ensure `pytest.ini` contains:
  ```
  [pytest]
  DJANGO_SETTINGS_MODULE = config.settings
  ```

## Project Structure

```
inventory-api/
├── assets/
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── models.py
│   └── ...
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tests/
│   └── test_assets.py
├── requirements.txt
└── README.md
```
