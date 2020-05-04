from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(min_length=2,max_length=32,label='İsim')
    last_name = forms.CharField(min_length=2,max_length=32,label='Soyisim')
    student_number = forms.CharField(label='Öğrenci Numarası',min_length=8,max_length=9)
    username = forms.CharField(min_length=3,max_length=16,label='Kullanıcı adı')
    password1 = forms.CharField(min_length=8,max_length=32,label='Şifre',widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8,max_length=32,label='Şifreyi doğrula',widget=forms.PasswordInput)
    email = forms.EmailField(label='ITÜ Maili')

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','student_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(label='İsim',min_length=2,max_length=50)
    last_name = forms.CharField(label='Soyisim',min_length=2,max_length=50)
    username = forms.CharField(label='Kullanıcı adı',min_length=2,max_length=50)

    class Meta:
        model = User
        fields = ['first_name','last_name','username']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(label='Bio',required=False,max_length=500,widget=forms.Textarea(attrs={'rows':3, 'cols': 15}))
    website_instagram = forms.URLField(label="Instagram ( https://instagram.com/.. )",required=False,max_length=100)
    website_facebook = forms.URLField(label="Facebook ( https://facebook.com/.. )",required=False,max_length=100)
    website_twitter = forms.URLField(label="Twitter ( https://twitter.com/.. )",required=False,max_length=100)

    class Meta:
        model = Profile
        fields = ['image','bio','website_instagram','website_facebook','website_twitter']
