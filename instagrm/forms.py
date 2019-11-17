from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
from pyuploadcare.dj.forms import ImageField

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3",
                                                               "placeholder":"First Name"}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3",
                                                               "placeholder":"Last Name"}))
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3",
                                                               "placeholder":"Username"}))
    email = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control mb-3",
                                                               "placeholder":"Email"}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class":"form-control mb-3",
                                                               "placeholder":"Password"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password",)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("profile_pic",)


class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea())
    image = ImageField(label='')

    class Meta:
        model = Post
        fields = ("caption", "image",)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Comment
        fields = ("comment",)