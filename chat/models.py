from django.db import models
from main.models import Teams
from accounts.models import Users

# Create your models here.


class ChatMesseges(models.Model):
    chat_number = models.ForeignKey('Chats', on_delete=models.DO_NOTHING)
    member_name = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=1000)
    time_sent = models.DateTimeField(auto_now_add=True)


class Chats(models.Model):
    team_name = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    message_text = models.ForeignKey(ChatMesseges, on_delete=models.DO_NOTHING)
