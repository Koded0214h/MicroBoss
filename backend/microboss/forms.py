from django import forms
from .models import CustomUser, Invites
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type']
        labels = {
            'username': 'Username',
            'email':'Email Address',
        }
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1']
        labels = {
            'username': 'Username',
            'email':'Email Address',
        }
        
class InviteForm(forms.ModelForm):
    class Meta:
        model = Invites
        fields = "__all__"
        labels = {
            'idea': 'Idea Description'
        }