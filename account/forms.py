from django import forms
from .models import *


class profilefunction(forms.ModelForm):
    class Meta:
        model=profile
        fields=['profile_photo','location','bio']
        # widgets={
        #     'profile_photo':forms.FileInput(attrs={'class':'form-control', 'placeholder':"enter your name"}),
        #     'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':"enter your title"}),
        #     'bio':forms.TextInput(attrs={'class':'form-control', 'placeholder':"write your content"}),
        # }