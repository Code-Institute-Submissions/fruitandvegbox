from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from newsletters.models import Newsletter


class NewsletterCreationForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'



class NewsletterCreationForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'subject',
            'body',
            'email',
            'status',
            )
