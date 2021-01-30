from django.db import models
from main.models import Teams
from accounts.models import Users


# Create your models here.

class ChatMessages(models.Model):

    chat_number = models.ForeignKey('Chats', on_delete=models.DO_NOTHING)
    member_name = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=1000)
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.time_sent.strftime("%Y-%m-%d %H:%M:%S") + " " + str(self.member_name) + ": " + self.message

      
class Chats(models.Model):
    team_name = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    # message_text = models.ForeignKey(ChatMessages, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Chat: " + str(self.team_name)

# class Meta:
#        ordering = ['time_sent']
#        message = models.CharField(max_length=1000)
