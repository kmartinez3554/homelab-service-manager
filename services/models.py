from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    
    description = models.TextField(blank=True)

    host = models.CharField(max_length=255)

    port = models.PositiveIntegerField()

    url = models.URLField(blank=True)

    service_type = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name