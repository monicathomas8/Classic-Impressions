from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactMessageForm
from django.shortcuts import redirect, render


def contact_view(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Notify client
            send_mail(
                f"New enquiry from {name}: {subject}",
                f"From: {name}\nEmail: {email}\n\nMessage:\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
            )

            # Confirmation email to customer
            send_mail(
                "We've received your message - Classic Impressions",
                f"Hi {name},\n\n"
                f"Thank you for getting in touch!\n\n"
                f"We've received your message regarding '{subject}':\n\n"
                f"{message}\n\n"
                f"We will respond within 48 hours.\n\n"
                f"Kind regards,\n"
                f"Classic Impressions",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

            messages.success(
                request,
                "Thank you. Your message has been sent. We aim to "
                "respond to all messages within 48 hours."
            )
            return redirect("contact")
    else:
        form = ContactMessageForm()

    return render(request, "contact/contact.html", {"form": form})
