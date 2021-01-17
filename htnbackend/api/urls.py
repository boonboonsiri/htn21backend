from django.urls import path
from . import views
from .views import DiscordUserAPIView, DayAPIView, HourAPIView,  CreateMessageAPIView, GetHourAPIView  
from .views import FilterMessageByUserAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', DiscordUserAPIView.as_view()),
    path('day/', DayAPIView.as_view()),
    path('hour/', HourAPIView.as_view()),
    path('positive/<str:user>', views.pos, name='pos'),
    path('negative/<str:user>', views.neg, name='neg'),
    path('createmessage', CreateMessageAPIView.as_view()),
    path('messages/<str:user>', FilterMessageByUserAPIView.as_view()),

    # Boon Paths
    path('gethour/<str:user>', GetHourAPIView.as_view())
    # Day, Month
]