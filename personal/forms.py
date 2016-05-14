from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from personal.models import Profile, StudentCard


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Enter email:")
    username = forms.CharField(label="Enter username:")
    password1 = forms.CharField(label="Enter your password:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Validate password:", widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)
    student_id = forms.CharField(label="Enter your student card id:", required=False)

    def __init__(self, _type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = _type
        self.setup_helper()

    def setup_helper(self):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

        if self.type == "Student":
            self.fields['avatar'].required = True
        else:
            self.fields['student_id'].label = "Enter your teachers id:"

    def clean(self):
        cleaned_data = super().clean()

        # Check username
        if Profile.objects.filter(user__username=cleaned_data['username']).exists():
            raise forms.ValidationError("Student with this username already exists")

        # Check student info
        if cleaned_data['type'] == "Student":
            try:
                StudentCard.object.get(card_id=cleaned_data['student_id'])
            except:
                raise forms.ValidationError("No such student card id in database")

            # Student must have avatar
            if not cleaned_data['avatar']:
                raise forms.ValidationError("You should upload avatar")

        # Validate passwords
        try:
            assert cleaned_data['password1'] == cleaned_data['password2']
        except:
            raise forms.ValidationError("Passwords are not equal")

        return cleaned_data

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password1'])
        student_info = StudentCard.objects.get(card_id=self.cleaned_data['student_id'])
        profile = Profile.objects.create(user=user,
                                         avatar=self.cleaned_data['avatar'],
                                         type=self.type,
                                         student_info=student_info)
        return profile
