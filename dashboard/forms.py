from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model= Notes
        fields= ['title','description']
        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }
        
class DateInput(forms.DateInput):
    input_type= 'date'        
        
class HomeworkForm(forms.ModelForm):
    class Meta:
        model= Homework
        fields= ['subject','title','description','due','is_finished']
        widgets={
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'due':DateInput(attrs={'class':'form-control'}),
        }
        
class DashboardForm(forms.Form):
    text= forms.CharField(max_length=200,label="Enter your search")
    
class TodoForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields= ['title','is_finished']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','password1','password2']