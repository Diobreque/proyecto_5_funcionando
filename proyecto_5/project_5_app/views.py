from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    form = forms.Registrousuario()
    if request.method == 'POST':
        form = forms.Registrousuario(request.POST)
        if form.is_valid():
            print("FORMULARIO OK !!!")
            print("Nombre")
            print("Email")
            print("Telefono")

    data = {"formulario": form}
    return render(request, 'index.html', data)
