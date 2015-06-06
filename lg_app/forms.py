from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from lg_app.models import *

class ComplejoAltaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComplejoAltaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_alta_complejo'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Confirmar'))
        self.helper.form_action = 'alta'
        self.helper.form_class='form-horizontal'
        self.helper.label_class='col-lg-1'
        self.helper.field_class='col-lg-4'

    class Meta:
        model = Complejo
        exclude = []
