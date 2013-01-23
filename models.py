from django.db import models
from django import forms
import datetime


CATEGORY_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class Event(models.Model):
	title = models.CharField(max_length=60)
	category = models.ForeignKey('Categories')
	length = models.TimeField(null=True, blank=True)
	counter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	counterUnit = models.CharField(max_length=15, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='hiking/', null=True, blank=True)
	timestamp = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return self.title

class Categories(models.Model):
	title = models.CharField(max_length=30)

	def __unicode__(self):
		return self.title

class EventForm(forms.Form):
	title = forms.CharField(max_length=60)
	category = forms.ModelChoiceField(queryset=Categories.objects.all())
	length = forms.TimeField(required=False)
	counter = forms.DecimalField(max_digits=20, decimal_places=2, required=False)
	counterUnit = forms.CharField(max_length=15, required=False)
	url = forms.URLField(required=False)
	description = forms.CharField(widget=forms.widgets.Textarea(), required=False)
	image = forms.FileField(widget=forms.ClearableFileInput, required=False)
	timestamp = forms.DateTimeField(initial=datetime.datetime.now, widget=forms.DateTimeInput)

class CategoriesForm(forms.Form):
	category = forms.CharField(max_length=30)

# categories (hiking, ran, movie)
# counterUnit (miles, laps, etc....)