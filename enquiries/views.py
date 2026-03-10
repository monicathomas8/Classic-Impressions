from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomServiceRequestForm


def custom_service_request_view(request):
    if request.method == "POST":
        form = CustomServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            request_type = form.cleaned_data['request_type']
            description = form.cleaned_data['description']

            # Email to client
            send_mail(
                f"New Custom Service Request from {name}",
                (
                    f"Name: {name}\nEmail: {email}\nType: {request_type}\n\n"
                    f"Description:\n{description}"
                ),
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
            )

            # Confirmation email to customer
            send_mail(
                "Your Request - Classic Impressions",
                f"""Hi {name},

Thank you for your request!
We've received your enquiry and will be in touch shortly.

Kind regards,
Classic Impressions""",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

            messages.success(
                request,
                "Thank you! We've received your request and will be in touch."
            )
            return redirect("custom_services")
    else:
        form = CustomServiceRequestForm()

    return render(request, "enquiries/custom_services.html", {"form": form})
