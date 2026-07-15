from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        label="Your Email ",
        max_length=50,
        widget=forms.EmailInput(attrs={'type':'email', 'name':'email', 'id':'email', 'placeholder':'you@example.com'})
    )
    message = forms.CharField(
        label="Message ",
        max_length=500,
        widget=forms.Textarea(attrs={'id':'message', 'name':'message', 'rows':'5', 'placeholder':'Write your feedback'})
    )
