from django.db import models
from django import forms


class MyImage(models.Model):
    model_img = models.ImageField(upload_to='img/', null=True, blank=True)


class InstagramImage(models.Model):
    instagram_photo = models.ImageField(upload_to='img/', null=True, blank=True)
    facebook_link = models.CharField(max_length=300, blank=True)
    instagram_link = models.CharField(max_length=300, blank=True)

#
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     phone = forms.CharField(max_length=100, required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)
