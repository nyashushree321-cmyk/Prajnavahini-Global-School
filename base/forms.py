from django import forms

from .models import Application, ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'classApplied', 'year', 'academicYear',
            'studentName', 'gender', 'dob', 'bloodGroup', 'motherTongue',
            'birthPlace', 'nationality', 'aadhaar',
            'fatherName', 'motherName', 'fatherMobile', 'motherMobile',
            'address', 'agree',
        ]
        widgets = {
            'classApplied': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'academicYear': forms.TextInput(attrs={'class': 'form-control'}),
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bloodGroup': forms.TextInput(attrs={'class': 'form-control'}),
            'motherTongue': forms.TextInput(attrs={'class': 'form-control'}),
            'birthPlace': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhaar': forms.TextInput(attrs={'class': 'form-control'}),
            'fatherName': forms.TextInput(attrs={'class': 'form-control'}),
            'motherName': forms.TextInput(attrs={'class': 'form-control'}),
            'fatherMobile': forms.TextInput(attrs={'class': 'form-control'}),
            'motherMobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'agree': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
