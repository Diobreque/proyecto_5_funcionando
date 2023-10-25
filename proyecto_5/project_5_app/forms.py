from django import forms

class Registrousuario(forms.Form):
    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloqueado', 'BLOQUEADO')]

    nombre = forms.CharField()
    telefono = forms.CharField(widget=forms.NumberInput)
    email = forms.CharField(widget=forms.EmailInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'