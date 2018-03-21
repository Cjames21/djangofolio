from django import forms

class ContactForm(forms.Form):
    First_name = forms.CharField(max_length=25)
    Last_name = forms.CharField(max_length=25)
    Phone = forms.CharField(required=False, max_length=30)
    Email = forms.EmailField()
    Subject = forms.CharField(max_length=100)
    Message = forms.CharField(widget=forms.Textarea)
    