from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):

    # first_name = forms.CharField(max_length=30, required=True, label="نام")
    # last_name = forms.CharField(max_length=150, required=True, label="نام خانوادگی")
    # email = forms.EmailField(required=False, label="ایمیل")

    # class Meta(UserCreationForm.Meta):
    #     model = User
    #     fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 4:
            raise forms.ValidationError(" نام نباید کمتر از 4 حرف باشد")
        return first_name
# ----------------------------------------------------------------------------