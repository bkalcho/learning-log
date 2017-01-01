# Author: Bojan G. Kalicanin
# Date: 01-Jan-2017

from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}