from django import forms
from .models import MainComment

class MainCommentForm(forms.ModelForm):
    content = forms.CharField(label='Yorum',widget=forms.Textarea(attrs={'rows':3, 'cols': 15}))

    class Meta:
        model = MainComment
        fields = ['content']
