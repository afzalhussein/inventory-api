from rest_framework import viewsets
from .models import Asset
from .serializers import AssetSerializer
from .permissions import IsAdminOrManager, IsViewerReadOnly
from .filters import AssetFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [IsViewerReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AssetFilter
    search_fields = ['name', 'serial_number', 'category']
    ordering_fields = ['created_at', 'updated_at', 'name']