from django import forms
from django.utils.translation import gettext_lazy as _
from .models import BlogContent,BlogContentImage,BlogModel


class UserChangeForm(forms.ModelForm):
    imageone = forms.FileField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = BlogContent
        fields = "__all__"
        # field_classes = {"username": UsernameField}
        
        
class BlogContentImageForm(forms.ModelForm):
    class Meta:
        model = BlogContentImage
        fields = ['image']

from django.forms.models import inlineformset_factory

BlogContentImageFormSet = inlineformset_factory(BlogContent, BlogContentImage, form=BlogContentImageForm, extra=1)

class BlogContentForm(forms.ModelForm):
    class Meta:
        model = BlogContent
        fields = ['type', 'imageone', 'imagetwo', 'content']

    def __init__(self, *args, **kwargs):
        super(BlogContentForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.attrs.update({'class': 'form-control'})
        self.fields['imageone'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagetwo'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})

        self.fields['imageone'].required = False
        self.fields['imagetwo'].required = False

        self.fields['imageone'].label = 'Image 1'
        self.fields['imagetwo'].label = 'Image 2'

        self.fields['content'].label = 'Content'

        # initialize formset
        self.instance.pk = kwargs['instance'].pk
        self.blog_content_image_formset = BlogContentImageFormSet(instance=self.instance, prefix='blog_content_image_formset')

    def is_valid(self):
        # add formset validation to form validation
        valid = super(BlogContentForm, self).is_valid()
        if self.blog_content_image_formset.is_valid():
            self.cleaned_data['blog_content_image_formset'] = self.blog_content_image_formset.cleaned_data
        else:
            valid = False
        return valid

    def save(self, commit=True):
        # save form data and formset data together
        blog_content = super(BlogContentForm, self).save(commit=False)
        if commit:
            blog_content.save()
        if self.cleaned_data.get('blog_content_image_formset'):
            for form in self.cleaned_data['blog_content_image_formset']:
                blog_content_image = form.save(commit=False)
                blog_content_image.content = blog_content
                if blog_content_image.image:
                    blog_content_image.save()
        return blog_content

BlogContentFormSet = forms.modelformset_factory(BlogContent, form=BlogContentForm, extra=1, can_delete=True)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['topic', 'slug', 'title', 'image', 'rating', 'created_date', 'content']

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['rating'].widget.attrs
