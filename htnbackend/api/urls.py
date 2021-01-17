from django.urls import path
from . import views
from .views import DiscordUserAPIView, DayAPIView, HourAPIView, PositiveWordsAPIView, NegativeWordsAPIView, CreateMessageAPIView    

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', DiscordUserAPIView.as_view()),
    path('day/', DayAPIView.as_view()),
    path('hour/', HourAPIView.as_view()),
    path('positive/', PositiveWordsAPIView.as_view()),
    path('negative/', NegativeWordsAPIView.as_view()),
    path('createmessage', CreateMessageAPIView.as_view())
]