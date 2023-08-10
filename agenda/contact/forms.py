from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)
        # fields = '__all__'

    # name = forms.CharField(widget=form.TextInput(attrs={'class':'input'}))




