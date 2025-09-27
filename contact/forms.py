from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}), label='Name')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(max_length=150, label='Subject')
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows':'5'}), label='Message')