from django import forms
from .models import CustomServiceRequest


class CustomServiceRequestForm(forms.ModelForm):
    class Meta:
        model = CustomServiceRequest
        fields = [
            "name",
            "email",
            "phone",
            "request_type",
            "description",
            "budget",
            "preferred_date",
        ]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
        }
