from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from hotels.forms import HotelRoomForm
from hotels.models import HotelRoom, Hotel, RoomReservation
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Manager


def manager_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "manager_login.html", context={"login_form": form})


def manager_signup(request):
    if request.method == 'POST':
        userform = forms.ManagerForm(request.POST)
        detailform = forms.ManagerDetailForm(request.POST)
        if userform.is_valid() and detailform.is_valid():
            user = userform.save()  # Save the User instance

            # Create Manager instance with associated User
            manager = Manager.objects.create(user=user, phone=detailform.cleaned_data['phone'],
                                             address=detailform.cleaned_data['address'])

            return redirect('homepage')
    else:
        userform = forms.ManagerForm()
        detailform = forms.ManagerDetailForm()

    return render(request, 'manager_signup.html', {'userform': userform, 'detailform': detailform})


def manager_logout(request):
    logout(request)
    return redirect("homepage")


def manage_hotels(request):
    manager_instance = Manager.objects.get(user=request.user)

    # Retrieve hotels managed by the logged-in manager
    hotels = Hotel.objects.filter(manager=manager_instance)

    return render(request, 'manage_hotels.html', {'hotels': hotels})


def reservation_list(request, hotel_id):
    hotel = Hotel.objects.get(pk=hotel_id)

    reservations = RoomReservation.objects.filter(hotel=hotel)

    return render(request, 'reservation_list.html', {'hotel': hotel, 'reservations': reservations})
