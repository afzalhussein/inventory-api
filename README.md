# inventory-api
Inventory Management API built with Django, DRF, PostgreSQL, JWT, RBAC, and pytest.

```text
inventory_api/
├── config/                      # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── assets/                      # Asset tracking app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── filters.py
│
├── users/                       # Custom User model
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   └── apps.py
│
├── tests/                       # Pytest tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_assets.py
│
├── manage.py
├── requirements.txt
└── README.md
```
