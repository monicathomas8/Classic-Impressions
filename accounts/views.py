from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from orders.models import Order


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
    """
    Displays the account details of the logged-in user.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(
        request,
        'accounts/my_account.html',
        {
            'user': request.user,
            'orders': orders,
        },
    )
