from django import forms

class IncidentLog(forms.Form):
    your_email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'ex. userid@gmail.com'}), label='Your email*')
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Who were the people involved?'}), label='Name(s)', max_length=100, required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Where did the incident occur?'}), label='Location', max_length=100, required=False)
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Provide some details/descriptors of the incident.', 'id': 'context', 'class': 'pure-input-1-2'}), label='Context/Situation')
    quote = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Was something specific said?'}), label='Quote')
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ex. #sexual harrassment, #bullying'}), label='Tags', max_length=50, required=False)
