""" Simple Model Serializers """
from rest_framework import serializers
from .models import DiscordUser, Day, Hour, Word, PositiveWords, NegativeWords, Message
from .vader import score_text


class DiscordUserSerializer(serializers.ModelSerializer):
    """ Serializer for documents to JSON """

    class Meta:
        model = DiscordUser
        fields = ['discord_id', 'positive', 'negative', 'last_updated']


class DaySerializer(serializers.ModelSerializer):
    """ Serializer for results """

    class Meta:
        model = Day
        fields = ['discord_user', 'date', 'day_number', 'average_score', 'word', 'time']
    

class HourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hour
        fields = ['hour_number', 'average_score', 'day']


class PositiveWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositiveWords
        fields = ['average_score', 'word']


class NegativeWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['average_score', 'word']


class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['messages', 'date', 'score', 'user']

    def create(self, validated_data):
        messages = validated_data['messages']
        print(messages)
        date = validated_data['date']
        score = validated_data['score']
        user = validated_data['user']
        time = validated_data['time']
        score = score_text(messages)['compound']
        
        message = Message(messages=messages,date=date,time=time, score=score,user=user)
        message.save()
        return message
        

