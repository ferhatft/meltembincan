from django import forms
from .models import Contact,Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'birthday','meseleginiz','boy','kilo','yatis_kalkis','mesai','yemek_saatleri','saglik_problemleri','operasyonlar','ilaçlar','sindirim','su','kahve_çay','alkol','sigara','istenen_besinler','istenyemen_besinler','diyet_gecmisi','message','message',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tam İsim *'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email *'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Numarası *'}),
            # 'subject': forms.ChoiceField(attrs={'placeholder': 'Talebiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesaj *','style': "height: 150px"}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = '*'




class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]
        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': ugettext_lazy('E-mail Adresiniz')}),
        # }

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'email form-control'