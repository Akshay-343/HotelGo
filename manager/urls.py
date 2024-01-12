from django.urls import path
from .views import manager_signup, manager_login, manager_logout, manage_hotels, reservation_list

urlpatterns = [
    path('manager/signup/', manager_signup, name='manager_signup'),
    path('manager/login/', manager_login, name='manager_login'),
    path('manager/logout/', manager_logout, name='manager_logout'),
    path('manager/hotels/', manage_hotels, name='manage_hotels'),
    path('hotel/reservations/<int:hotel_id>/', reservation_list, name='reservation_list'),
]



