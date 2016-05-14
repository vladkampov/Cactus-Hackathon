from django import forms
from django.contrib.auth.models import User
from personal.models import Profile, StudentCard


class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    type = forms.CharField()
    avatar = forms.ImageField()
    student_id = forms.CharField()

    def clean(self):
        import ipdb; ipdb.set_trace()
        cleaned_data = super().clean()

        # Check username
        if Profile.objects.filter(user__username=cleaned_data['username']).exists():
            raise forms.ValidationError("Student with this username already exists")

        # Check student info
        if cleaned_data['type'] == "Student":
            try:
                StudentCard.object.get(card_id=cleaned_data['student_id'])
            except StudentCard.DoesNotExists:
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

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password1'])
        student_info = StudentCard.objects.get(card_id=self.cleaned_data['student_id'])
        profile = Profile.objects.create(user=user,
                                         avatar=self.cleaned_data['avatar'],
                                         type=self.cleaned_data['type'],
                                         student_info=student_info)
        return profile
