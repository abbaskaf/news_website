from django import forms


class ShareForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    description = forms.CharField( required=False, widget=forms.Textarea)