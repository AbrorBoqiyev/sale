from django import forms
from .models import *


class BlogsForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = '__all__'