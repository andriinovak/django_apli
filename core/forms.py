from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    age = forms.IntegerField(label='age', min_value=1)
    status = forms.ChoiceField(
    label="Your status",
    choices=((1, "Not relevant"),
             (2, "Review"),
             (3, "Maybe relevant"),
             (4, "Relevant"),
             (5, "Leading candidate")))
    message = forms.CharField(label='Message', widget=forms.Textarea)


