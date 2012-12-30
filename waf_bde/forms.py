from django import forms
from commons import happyforms

class ContactForm(happyforms.Form):
    subject = forms.CharField(
        max_length=100,
        label=u'Sujet')

    message = forms.CharField(
        widget=forms.Textarea,
        label=u'Message')

    honeypot = forms.CharField(
        required=False,
        label=" ",
        widget=forms.TextInput(attrs={'class': 'hidden'}))

    def clean_honeypot(self):
        value = self.cleaned_data['honeypot']
        if value:
            raise forms.ValidationError('Spam attempt detected!')
        return value
