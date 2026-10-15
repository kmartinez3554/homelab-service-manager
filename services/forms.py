from django import forms

from .models import Service

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = [
            'name',
            'description',
            'host',
            'port',
            'url',
            'service_type',
            'is_active',
        ]