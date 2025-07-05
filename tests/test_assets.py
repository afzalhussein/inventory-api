import pytest
from rest_framework.test import APIClient
from assets.models import Asset

@pytest.mark.django_db
def test_asset_list(user):
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get('/api/assets/')
    assert response.status_code == 200