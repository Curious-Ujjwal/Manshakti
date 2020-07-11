from django import forms
from .models import *

class storyForm(forms.ModelForm):
	class Meta:
		model = Story
		fields = ['name','city','inbox']