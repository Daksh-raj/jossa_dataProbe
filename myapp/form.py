from django import forms  
from myapp.models import Student

class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"