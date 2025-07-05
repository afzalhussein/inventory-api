from django.db import models

class Asset(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'In Stock'),
        ('in_use', 'In Use'),
        ('damaged', 'Damaged'),
        ('disposed', 'Disposed'),
    )

    name = models.CharField(max_length=255, db_index=True)
    serial_number = models.CharField(max_length=100, unique=True, db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, db_index=True)
    assigned_to = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['category', 'status']),
            models.Index(fields=['name', 'serial_number']),
        ]