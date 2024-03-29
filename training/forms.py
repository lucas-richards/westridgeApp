from django import forms
from .models import CertificationStatus, Certification


class StatusUpdateForm(forms.ModelForm):
    completed_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = CertificationStatus
        fields = ['completed_date']

class UploadFileForm(forms.Form):
    file = forms.FileField()

#  certification update form
class CertificationUpdateForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Certification
        fields = ['name', 'description', 'exp_months', 'scheduled_date', 'roles']

#  schedule certification form
class ScheduleCertificationForm(forms.ModelForm):
    scheduled_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Certification
        fields = ['scheduled_date']


