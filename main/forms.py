from django import forms

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label="Email Address")


from django import forms

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label="Email Address")

class NewsletterForm(forms.Form):
    subject = forms.CharField(
        max_length=255,
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )