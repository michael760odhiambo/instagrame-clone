from django import forms
from .models import Profile,Comment

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'body',)