from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import  View
from .forms import  LoginForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import User
from .forms import UserRegisterForm
from django.contrib import messages


class loginUser(FormView):
    template_name = 'login/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self,form):

        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request,user)
        return super(loginUser,self).form_valid(form)


"""
Al apretar el botón cerrar sesión en cualquier template, se redirige a 
una página vacía de logout que redirige automáticamente al login
"""
class LogoutView(View):

    def get(self,request,*args,**kargs):
        """
        Cada vez que se cierra sesión se borrar el historial del Panel izquierdo.
        editando el archivo historial.json a {}
        """
        import json
        with open('static/json/historial.json','w') as f:
            json.dump({},f)
        logout(request)

        return HttpResponseRedirect(reverse('login_app:login'))


def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                messages.success(request, f'Usuario {username} creado')
                asunto = 'Verificacion de usuario'
                form.save()
                username = request.POST.get('username',)
                nombre = request.POST.get('nombre',)
                primerApellido = request.POST.get('primerApellido',)
                segundoApellido = request.POST.get('segundoApellido',)
                id_usuario = User.objects.filter(
                    username =username
                ).values('id')
                id_usuario = list(id_usuario)[0]['id']

                nombreCompleto = nombre + ' ' + primerApellido + ' ' + segundoApellido
                mensaje = """
                Estimado XXXXXX,

                Ha sido creada una cuenta a la página de CFM a nombre de %s.

                Favor de resolver su solicitud en el siguiente link:

                http://127.0.0.1:8000/editar-usuario/%d
                """ % (nombreCompleto,id_usuario)
                
                email_remitente = 'servicioclientecfm@gmail.com'
                email_destinatario = ['servicioclientecfm@gmail.com']
                send_mail(asunto, mensaje, email_remitente, email_destinatario,)
                return redirect('/')
        else:
            form = UserRegisterForm()

        context = { 'form' : form }
        return render(request, 'login/register.html', context)
































# from django.views.generic import TemplateView
# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import (
#     get_user_model,
#     login,
#     authenticate,
# )



"""
Login CFM  
"""
# def login(request):
#     """
#     Autentificar usuario
#     """
    
#     #user = authenticate(username=username, password=password)
   
#     """
#     Cada vez que se cierra sesión se borrar el historial del Panel izquierdo.
#     editando el archivo historial.json a {}
#     """
#     import json
#     with open('static/json/historial.json','w') as f:
#         json.dump({},f)


#     return render(request,'login/login.html')