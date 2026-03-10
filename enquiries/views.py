from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomServiceRequestForm


def custom_service_request_view(request):
    if request.method == "POST":
        form = CustomServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! We’ve received your request and will be in touch."
            )
            return redirect("custom_services")
    else:
        form = CustomServiceRequestForm()

    return render(request, "enquiries/custom_services.html", {"form": form})
