from tkinter import Widget
from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['Topic_name','Name']
        #widgets={'Email':forms.PasswordInput}
        #widgets={'Topic_name':forms.RadioSelect}

        




