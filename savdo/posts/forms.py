from django import forms
from .models import *


class PostsForm(forms.ModelForm):
    title = forms.CharField(help_text="Title of your post",widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title'}))
    content = forms.CharField(help_text="Write about your post and your post content", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Give some ideas here...'}))
   
    
    class Meta():
        model = Posts
        fields = ('title', 'content')
        
