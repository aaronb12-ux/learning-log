from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm): #class 'TopicForm' that inherits from 'forms.ModelForm'
    class Meta:
        model = Topic #build a form from the Topic Model
        fields = ['text'] #including only a text field
        labels = {'text': ''} #don't generate a label for the 'text' field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        #a widgets is an HTMl form elements like a single line text box
        #using forms.Textarea to customize the text box space