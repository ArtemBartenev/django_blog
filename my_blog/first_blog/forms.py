from django import forms
from .models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        data = self.cleaned_data.get("slug").lower()
        if data == 'create':
            raise ValidationError('Slug must not be "Create"')
        return data
    
    def save(self):
        new_tag = Tag.objects.create(
                title=self.cleaned_data["title"],
                slug=self.cleaned_data['slug'])

        return new_tag
