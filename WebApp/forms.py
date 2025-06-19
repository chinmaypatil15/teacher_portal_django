from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'subject', 'marks']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100
            }),
        }

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks is not None and (marks < 0 or marks > 100):
            raise forms.ValidationError("Marks should be between 0 and 100.")
        return marks


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'subject', 'marks']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter student name'
#             }),
#             'subject': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter subject'
#             }),
#             'marks': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter marks',
#                 'min': '0',
#                 'max': '100'
#             })
#         }
        
#     def clean_marks(self):
#         marks = self.cleaned_data.get('marks')
#         if marks is not None and (marks < 0 or marks > 100):
#             raise forms.ValidationError("Marks should be between 0 and 100")
#         return marks

#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         subject = cleaned_data.get('subject')
        
#         if self.instance.pk:  # Editing existing instance
#             if Student.objects.filter(name=name, subject=subject).exclude(pk=self.instance.pk).exists():
#                 raise forms.ValidationError("A student with this name and subject already exists.")
#         else:  # Creating new instance
#             if Student.objects.filter(name=name, subject=subject).exists():
#                 raise forms.ValidationError("A student with this name and subject already exists.")
        
#         return cleaned_data
