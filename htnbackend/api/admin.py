from django.contrib import admin

# Register your models here.
from .models import DiscordUser, Word, Day, Hour, PositiveWords, NegativeWords, Message

admin.site.register(DiscordUser)
admin.site.register(Word)
admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(PositiveWords)
admin.site.register(NegativeWords)
admin.site.register(Message)
