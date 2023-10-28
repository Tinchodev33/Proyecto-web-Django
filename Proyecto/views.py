from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from tienda.forms import CustomUserCreationForm

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect(to='Home')
            else:
                messages.error(request, "Hubo un problema con la autenticación del usuario.")
        else:
            messages.error(request, "El formulario no es válido. Por favor, revisa los datos ingresados.")
    return render(request, 'registration/registro.html', data)
