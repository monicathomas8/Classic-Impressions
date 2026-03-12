from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from orders.models import Order
from contact.forms import ContactMessageForm
from django.core.mail import send_mail
from django.conf import settings


def signup(request):
    """
    Allows a new customer to create an account
    using Django's built-in
    User model and UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Account created for {username}! You can now login'
            )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout_user(request):
    """
    Logs out the current user and redirects to home page.
    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


@login_required
def my_account(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                f"New enquiry from {name}: {subject}",
                f"From: {name}\nEmail: {email}\n\nMessage:\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
            )

            messages.success(request, "Your message has been sent!")
            return redirect('my_account')
    else:
        form = ContactMessageForm(initial={
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        })

    return render(
        request,
        'accounts/my_account.html',
        {
            'user': request.user,
            'orders': orders,
            'form': form,
        },
    )
