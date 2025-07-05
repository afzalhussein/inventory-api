import django_filters
from .models import Asset

class AssetFilter(django_filters.FilterSet):
    class Meta:
        model = Asset
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
            'status': ['exact'],
        }
        