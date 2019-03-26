from college.models import StudentProfile
from django import forms


class StudentForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = StudentProfile
        fields = [
            "first_name",
            "profile_pic",
            "aadhar",
            "last_name",
            "startstation",
            "endstation",
            "pass_out",
            "department",
            "issued",
            #"contact"
        ]
    """def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        first_name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')"""
