from django.contrib import admin
from .models import Chats, ChatMessages

# Register your models here.
admin.site.register(Chats)
admin.site.register(ChatMessages)