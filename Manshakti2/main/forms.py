from django import forms
from .models import *
from crispy_forms.helper import FormHelper

class storyForm(forms.ModelForm):

	class Meta:
		model = Story
		fields = ['name','city','subject','inbox']
		labels = {
			'name': '',
			'city': '',
			'subject': '',
			'inbox': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control specific', 'placeholder': 'Name(Optional)'}),
			'city': forms.TextInput(attrs={'class': 'form-control specific', 'placeholder': 'City'}),
			'subject': forms.TextInput(attrs={'class': 'form-control specific', 'placeholder': 'Subject'}),
			'inbox': forms.Textarea(attrs={'class': 'form-control specific specifictext', 'placeholder': 'Type Here', 'rows': '5'}),
		}