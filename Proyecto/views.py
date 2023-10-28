from email import message
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from tienda.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["form"] = formulario
            user = authenticate(usernam=formulario.cleaner_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.succes(request,"Te has registrado correctamente")
            return redirect(to='Home')
           
    
        return render(request, 'registration/registro.html', data)