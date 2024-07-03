from django import forms

CHOICES = (
    ('1', 'Male'),
    ('2', 'Female'),
    ('3', 'Other'),
)

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label='First Name', max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': "First name"}))
    last_name = forms.CharField(label='Last Name', max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(label='age', 
                             widget=forms.NumberInput(attrs={'placeholder': 'age'}))
    email = forms.CharField(label="email", max_length=100,
                            widget=forms.TextInput(attrs={'placehlder': "email"}))                            
    choice = forms.ChoiceField(choices=CHOICES, label='Gender',
                               widget=forms.Select(attrs={'class': 'form-select'}))
    # image = forms.ImageField(label='image', widget=forms.FileInput(
    #                            attrs={'class': 'form-control'}))                               
    
    def is_valid(self) -> bool:
        return super.is_valid()