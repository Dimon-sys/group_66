from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']

        def __init__(self, *args, **kwargs):
            super(AdvertisementForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class':'form-control'})
            self.fields['description'].widget.attrs.update({'class':'form-control form-control-lg'})
            self.fields['price'].widget.attrs.update({'class':'form-control form-control-lg'})
            self.fields['auction'].widget.attrs.update({'class':'form-check-input'}, required=False)
            self.fields['image'].widget.attrs.update({'class':'form-control form-control-lg'})

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError('Заголовок не может начинаться с вопросительного знака')
        return title


    