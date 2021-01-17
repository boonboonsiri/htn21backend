from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=1000, default=' ')
    score = models.DecimalField(max_digits=5, decimal_places=2)


#Create your models here
class Day(models.Model):
    discord_user = models.CharField(max_length=1000)
    date = models.DateField()
    day_number = models.IntegerField()
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    #words = models.ManyToManyField(Word) THis was pain
    time = models.TimeField()


class Hour(models.Model):
    hour_number = models.IntegerField()
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)


class PositiveWords(models.Model):
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


class NegativeWords(models.Model):
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


# Filter everything in the month
class DiscordUser(models.Model):
    discord_id = models.CharField(max_length=1000)
    positive = models.OneToOneField(PositiveWords, on_delete=models.CASCADE)
    negative = models.OneToOneField(NegativeWords, on_delete=models.CASCADE)
    last_updated = models.DateField()


class Message(models.Model):
    messages = models.CharField(max_length=1000, default=' ')
    date = models.DateField()
    time = models.TimeField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.CharField(max_length=1000, default=' ')


# Four graphs




