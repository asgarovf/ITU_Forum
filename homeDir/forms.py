from django import forms
from .models import MainPost

class MainPostForm(forms.ModelForm):
    title = forms.CharField(label='Başlık')
    content = forms.CharField(label='Yazı',widget=forms.Textarea(attrs={'rows':12, 'cols': 15}))
    url = forms.URLField(label='Link: https://...',required=False)
    tag = forms.CharField(label='Tag - #',required=False,max_length=50,widget=forms.Textarea(attrs={'rows':1, 'cols': 15}))

    class Meta:
        model = MainPost
        fields = ['title','content','url','tag']
