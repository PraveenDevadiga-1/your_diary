from django import forms
from django.contrib.auth.models import User
from your_diary_app.models import Diary_Page

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
    class Meta():
        model=User
        fields=('username','email','password')

class Diary_Page_Form(forms.ModelForm):
    note=forms.CharField(widget=forms.Textarea)
    DATE_INPUT_FORMATS = ['%d-%m-%Y']
    date=forms.DateField(input_formats=DATE_INPUT_FORMATS)
    class Meta():
        model=Diary_Page
        fields=('name','date','title','note')
