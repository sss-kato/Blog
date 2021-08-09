from django.forms import ModelForm
from django.forms.models import model_to_dict 
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']
