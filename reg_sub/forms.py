from django import forms
from reg_sub.models import Intern, Subscribe
import re




class internform(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=40, required=True)
    contactno = forms.CharField(max_length=15, required=False)
    interests = forms.CharField(max_length=100, required=True, widget=forms.Textarea)
    def clean_email(self):
        email2 = self.cleaned_data['email']
        try:
            flag = Intern.objects.get(email=email2)
        except Intern.DoesNotExist:
            flag = None
        if flag is not None:
            raise forms.ValidationError("Email exists")
        return email2

    def __init__(self, *args, **kwargs):
        super(internform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Name'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'E-mail address'})
        self.fields['contactno'].widget.attrs.update({'class' : 'form-control', 'placeholder': '+99-9999999999'})
        self.fields['interests'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Your Interests'})

class subform(forms.Form):
    error_css_class = 'help-block with-errors'
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=40, required=True)
    subject = forms.CharField(max_length=100, required=True)
    def clean_email(self):
        email2 = self.cleaned_data['email']
        try:
            flag = Subscribe.objects.get(email=email2)
        except Subscribe.DoesNotExist:
            flag = None
        if flag is not None:
            raise forms.ValidationError("Email exists")
        return email2

    def __init__(self, *args, **kwargs):
        super(subform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Your Email'})
        self.fields['subject'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'Subject'})
