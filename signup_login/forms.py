from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)



from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'mobile_number', 'password', 'confirm_password')
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        if not mobile_number.isdigit():
            raise forms.ValidationError("Invalid mobile number")
        return mobile_number

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        if len(otp) != 6 or not otp.isdigit():
            raise forms.ValidationError("Invalid OTP")
        return otp
