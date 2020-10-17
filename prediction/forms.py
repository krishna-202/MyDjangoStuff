from django import forms
from .models import approvals

class ApprovalsForm(forms.ModelForm):
    class Meta():
        model=approvals
        fields='__all__'
