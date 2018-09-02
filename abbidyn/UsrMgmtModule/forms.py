from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class RegistrationForm(UserCreationForm):

    # email = forms.EmailField(required=True)
    # address = forms.TextField(required=True)
    # pincode = forms.IntegerField(max_length=6, validators=[MinLengthValidator(6)])
    # isCook = forms.BooleanField(required=False,initial=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone_number','address','pincode','is_cook','password1','password2')

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     user.phone_number = self.cleaned_data['phone_number']
    #     user.address = self.cleaned_data['address']
    #     user.pincode = self.cleaned_data['pincode']
    #     user.is_cook = self.cleaned_data['is_cook']
    #
    #
    #     if commit:
    #         user.save()
    #
    #     return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
