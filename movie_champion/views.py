from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login

now = timezone.now()


def home(request):
    return render(request, 'movie_champion/home.html',
                  {'movie_champion': home})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'movie_champion/register_done.html', {'new_user': new_user})
    else:
      user_form = UserRegistrationForm()
      return render(request, 'movie_champion/register.html', {'user_form': user_form})


def movie_list(request):
    movie = Movie.objects.filter(created_date__lte=timezone.now())
    return render(request, 'movie_champion/movie_list.html',
                  {'movies': movie})


def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'movie_champion/customer_list.html',
                  {'customers': customer})


def cart(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'movie_champion/cart.html',
                  {'customers': customer})