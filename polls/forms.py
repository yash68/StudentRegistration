from django import forms
from .models import Student
from django.contrib.auth.models import User

class SampleForm(forms.Form):
	name = forms.CharField(max_length=30)
	email = forms.EmailField()
	zipcode = forms.CharField(max_length=30)


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    email=forms.CharField(widget=forms.EmailInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput
                            (attrs={'class': 'form-control'}),
                            label="Confirm your password",
                            max_length=30,
                            required=True)

    def clean_confirm_password(self):
        p = self.cleaned_data['password']
        cp = self.cleaned_data['confirm_password']
        if p!=cp:
            raise forms.ValidationError("Password and Confirm Password Must be Same")

    class Meta:
        model=User
        fields=['username','email','password','confirm_password',]