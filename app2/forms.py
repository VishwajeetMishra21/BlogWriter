from django import forms
from . models import Blogs


class Edit_Blog(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','dsc')