from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(label="email", max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': "email"}))                            
    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Passwrod', max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))