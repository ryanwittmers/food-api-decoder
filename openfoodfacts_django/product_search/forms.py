from django import forms

class BarcodeForm(forms.Form):
    barcode = forms.CharField(label='Enter barcode', max_length=100)
