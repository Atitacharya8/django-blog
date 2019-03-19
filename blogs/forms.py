from django import forms
from .models import *

class BlogForm(forms.ModelForm):
	class Meta:
		model=Blog
		fields=['title','image','content','author']

class ReviewForm(forms.ModelForm):
	class Meta:
		model=Review
		fields=["review"]


