from django.contrib import messages
from .forms import ContactMessageForm
from django.shortcuts import redirect, render


def contact_view(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. Your message has been sent.")
            return redirect("contact:contact")
    else:
        form = ContactMessageForm()

    return render(request, "contact/contact_form.html", {"form": form})
