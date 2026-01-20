from django.urls import path
from . import views

app_name = "requests"

urlpatterns = [
    path("", views.custom_service_request_view, name="custom_services"),
]
