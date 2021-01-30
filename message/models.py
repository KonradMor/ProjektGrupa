from django.db import models
from accounts.models import Users
# Create your models here.
class Messages(models.Model):
    id_user_from = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='message_from')
    id_user_to = models.ForeignKey(Users, models.DO_NOTHING, related_name='message_to')
    content = models.CharField(max_length=1000)
    sent_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content