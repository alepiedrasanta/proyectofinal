from django import forms
from .models import compus

class computadorasform(forms.ModelForm):
    class Meta:
        model = compus
        fields = ('marca', 'detalle', 'precio',)
