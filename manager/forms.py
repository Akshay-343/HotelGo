from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hotels.models import HotelRoom
from .models import Manager


class ManagerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class ManagerDetailForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ["address", "phone"]


class HotelRoomForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = ['hotel', 'room_type', 'available_rooms']
