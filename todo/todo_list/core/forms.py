from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ("title","description","priority_list","use_date")
