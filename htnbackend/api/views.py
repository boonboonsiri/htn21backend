from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import DiscordUserSerializer, DaySerializer, HourSerializer
from .serializers import PositiveWordSerializer, NegativeWordSerializer, CreateMessageSerializer
from .models import DiscordUser, Word, Day, Hour, PositiveWords, NegativeWords, Message


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DiscordUserAPIView(generics.ListAPIView):
    serializer_class = DiscordUserSerializer
    queryset = DiscordUser.objects.all()


class DayAPIView(generics.ListAPIView):
    serializer_class = DaySerializer
    queryset = Day.objects.all()


class HourAPIView(generics.ListAPIView):
    serializer_class = HourSerializer
    queryset = Hour.objects.all()


class PositiveWordsAPIView(generics.ListAPIView):
    serializer_class = PositiveWordSerializer
    queryset = PositiveWords.objects.all()


class NegativeWordsAPIView(generics.ListAPIView):
    serializer_class = NegativeWordSerializer
    queryset = NegativeWords.objects.all()


class CreateMessageAPIView(generics.CreateAPIView):
    serializer_class = CreateMessageSerializer
    queryset = Message.objects.all()
