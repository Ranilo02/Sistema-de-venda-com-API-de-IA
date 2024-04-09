from django import forms
from instruments.models import Instrument



class InstrumentModelForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = '__all__'


    def __init__(self, *args, **kwargs):
            super(InstrumentModelForm, self).__init__(*args, **kwargs)

            # placeholder da bio
            self.fields['bio'].widget.attrs['placeholder'] = 'Descreva seu produto ou deixe em branco para que nossa inteligência artificial o descreva...  OBS: esse recurso requer uma chave API'
            