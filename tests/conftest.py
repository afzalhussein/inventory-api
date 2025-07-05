import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        username='testuser',
        password='testpass123',
        role='viewer'
    )

@pytest.fixture
def admin_user():
    return get_user_model().objects.create_superuser(
        username='admin',
        password='adminpass123',
        role='admin'
    )