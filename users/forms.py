from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import ProfileModel

class NoHelpTextPasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        kwargs['render_value'] = True
        super().__init__(*args, **kwargs)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': NoHelpTextPasswordInput(),
            'password2': NoHelpTextPasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label="Remember me")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email']:
             self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['profile_image']




# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms




# class SignUpForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         for fieldname in ['username', 'email', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None