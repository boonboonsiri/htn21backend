from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import DiscordUserSerializer, DaySerializer, HourSerializer
from .serializers import CreateMessageSerializer, MessageSerializer 
from .models import DiscordUser, Word, Day, Hour, PositiveWords, NegativeWords, Message
from .vader import score_words
import json
from django.http import HttpResponse

from datetime import datetime

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


class CreateMessageAPIView(generics.CreateAPIView):
    serializer_class = CreateMessageSerializer
    queryset = Message.objects.all()


class FilterMessageByUserAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def filter_queryset(self, queryset):
        user = self.kwargs["user"]
        return queryset.filter(user__iexact=user)

class GetDayWeekAPIView(generics.ListAPIView):
    serializer_class = DaySerializer 
    queryset = Message.objects.all()

    def filter_queryset(self, queryset):
        user = "maya1" # Hardcode user probably (ALOT OF HARD CODING)

        messages =  queryset.filter(user__iexact=user)

        curDay = datetime.now().day 
        

        dayRet = []

        for i in range(7):
            numMessage = 0;
            totalSum = 0;
            for m in messages:
                curDay =  datetime.now().day - 7 + i;
                #nextDay = curDay - 7 + i + 1; # this will break by the end of the month

                mDay = datetime.strptime(str(m.date),  '%Y-%m-%d').day
                print(curDay)

                if(mDay == curDay):
                    numMessage += 1
                    totalSum += m.score

            #w.name = ""
            #w.score = 0
            if(numMessage != 0): # set for 1 so non zero
                w = Word();
                d = Day();
                d.discord_user = user
                #d.date
                d.day_number = i
                d.average_score = totalSum/numMessage
                #d.words.set(w)
                #time = models.TimeField()
                dayRet.append(d)
 
        print(dayRet)
        return dayRet
        


class GetHourAPIView(generics.ListAPIView):
    serializer_class = HourSerializer
    queryset = Message.objects.all()

    def filter_queryset(self, queryset):
        user = self.kwargs["user"]
        messages =  queryset.filter(user__iexact=user)
        curDay = datetime.now().date()
        hourRet = []
        for i in range(24):
            numMessage = 0;
            totalSum = 0;
            for m in messages:
 
                curHour =  datetime.strptime(str(curDay) + " " + str(i), '%Y-%m-%d %H')
                nextHour = datetime.strptime(str(curDay) + " " + str(i) + ":59" , '%Y-%m-%d %H:%M')

                mDate = m.date
                mTime = m.time

                mDateTime = datetime.strptime(str(mDate) + " " + str(mTime), '%Y-%m-%d %H:%M:%S')


                if(mDateTime >= curHour and mDateTime < nextHour):
                    numMessage += 1
                    totalSum += m.score
            #word ={
            #    "name" : "",
            #    "score" : 0
            #}
            w = Word();
            d = Day();
            h = Hour();


            w.name = ""
            w.score = 0

            d.discord_user = user;
            d.date = str(datetime.now().date())
            d.day_number = 0;
            d.average_score = 0;
            #d.words = w;

            if(numMessage != 0): # set for 1 so non zero
                print(i)
                h.hour_number = i;
                h.average_score = totalSum/numMessage 
                h.day = d
                hourRet.append(h)
 
    
        print(hourRet)
        return hourRet
            




def pos(request, user):
    queryset = Message.objects.all().filter(user__iexact=user)

    word = {}

    for x in queryset:
        lst = score_words(x.messages)
        for y in lst:
            if lst[y]['compound'] > 0:
                word[y] = lst[y]['compound']
    

    return HttpResponse(json.dumps(word), content_type="application/json")



def neg(request, user):
    queryset = Message.objects.all().filter(user__iexact=user)

    word = {}

    for x in queryset:
        lst = score_words(x.messages)
        for y in lst:
            if lst[y]['compound'] < 0:
                word[y] = lst[y]['compound']
    

    return HttpResponse(json.dumps(word), content_type="application/json")
    

