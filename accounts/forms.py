from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.core.exceptions import ValidationError
from django.forms import BooleanField
from .models import Users


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'username']

    is_boss = BooleanField(label='Please, select the checkbox only if you are a Boss', required=False)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        is_boss = self.cleaned_data['is_boss']
        user = Users(is_boss=is_boss, user=result)
        if commit:
            user.save()
        return result

    def boss_validation(self):
        is_boss = self.cleaned_data['is_boss']
        boss_counter = Users.objects.filter(is_boss=True).count()
        if boss_counter > 0:
            raise ValidationError("You are not a Boss, please deselect the checkbox")
        return is_boss
