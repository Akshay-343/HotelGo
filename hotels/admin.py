from django.contrib import admin
from .models import Hotel, RoomType, HotelRoom, RoomReservation
from manager import models as manager
admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(HotelRoom)
admin.site.register(RoomReservation)
admin.site.register(manager.Manager)
