from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
# class MessageForm(forms.Form):
#     full_name = forms.CharField(label="نام و نام خانوادگی")
#     email = forms.EmailField(label="ایمیل")
#     subject = forms.CharField(label="عنوان پیام") 
#     message = forms.CharField(widget=forms.Textarea,label="متن پیام")






# def validate_full_name(value):
#     if len(value.split()) < 2:
#         raise ValidationError(
#             code='invalid_full_name'
#         )
class MessageForm(forms.ModelForm):

    #     full_name = forms.CharField(
    #     label="نام و نام خانوادگی",
    #     validators=[validate_full_name], 
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
    def clean_full_name(self):
        self.fullname_data = self.cleaned_data.get('full_name')
        if len(self.fullname_data) < 4 :
            raise ValidationError("نام شما حداقل باید 4 کارکتر باشد")
        return self.fullname_data