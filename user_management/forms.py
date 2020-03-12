from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Required, Please provide a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            self.fields[key].widget.attrs.update({'class': 'form-input'})

        # setting place-holders
        self.fields['username'].widget.attrs.update({'placeholder': 'john.doe'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'John'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Doe'})
        self.fields['email'].widget.attrs.update({'placeholder': 'johndoe123@example.com'})
        self.fields['password1'].help_text = None
        self.fields['password1'].widget.attrs.update({'placeholder': 'Difficult@Password123'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Difficult@Password123'})
