from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('room/<str:code>/', views.getRoom, name='get-room'),
    path('rooms/', views.RoomView.as_view(), name='all-rooms')
]
