from django.shortcuts import render


def home(request):
    """
    Simple homepage for the base project.
    Later you can expand this with hero, sections, etc.
    """
    return render(request, 'home.html')


def about(request):
    """
    Simple about page for the project.
    """
    return render(request, 'about.html')


def faq(request):
    """
    Simple FAQ page for the project.
    """
    return render(request, 'faq.html')


def installation(request):
    """
    Simple installation guide page for the project.
    """
    return render(request, 'installation.html')


def contact_view(request):
    """
    Simple contact page for the project.
    """
    return render(request, 'contact/contact.html')
