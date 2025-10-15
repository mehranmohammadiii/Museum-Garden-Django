from django import forms
from .models import Memory,MemoryGallery

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['title','text']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'})
        }

ImageFormSet = forms.inlineformset_factory  (
    Memory,
    MemoryGallery,
    fields = ('image_name',),
    extra=3,
    can_delete=False
                    )