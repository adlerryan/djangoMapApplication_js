from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserLocationRank, LocationUser, Location
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class RankLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocationRank
        fields = ['location', 'rank']
        widgets = {
            'location': forms.Select(choices=[(location.id, location.name) for location in LocationUser.objects.all()]),
        }