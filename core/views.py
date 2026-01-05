from django.shortcuts import render


def home(request):
    """
    Simple homepage for the base project.
    Later you can expand this with hero, sections, etc.
    """
    return render(request, 'home.html')
