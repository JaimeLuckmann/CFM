from django.urls.base import reverse_lazy
from django.shortcuts import render, redirect 
from applications.pieza.models import filaCarrito
from django.views.generic import ListView, DeleteView, UpdateView
from applications.login.models import User
from django import forms

def home(request):

    usuarioActivo = request.user 

    """
    Esto impide que un usuario no registrado 
    pueda acceder a las páginas
    """
    if not request.user.is_authenticated:
        return redirect('login_app:login')

    """
    Las siguientes líneas regresan al archivo historial.json
    a un {} vacío. Aplica un "reset" al Historial.

    El archivo context es devuelto a base.html para que se 
    agregue o actualice el historial en el panel izquierdo.
    """
    context = {}
    import json
    with open('static/json/historial.json','r') as f:
            context['historial'] = json.load(f)
    

    """
    Eliminar fila del carrito
    """
    eliminarFila = request.GET.get('eliminar','')
    id_eliminar = request.GET.get('id-eliminar','')
    if len(eliminarFila)>0:
        filaCarrito.objects.fila_segun_descripcion(eliminarFila,id_eliminar,usuarioActivo).delete()

    """
    Realiza una petición a la tabla filaCarrito en la base de datos y
    retorna todas las tareas con sus respectivos precios filtrando
    por el usuario que tenga la sesión activa para que al cerrar sesión
    o cambiar de usuario no pierda su cotización.
    """
    context['fila'] = filaCarrito.objects.tareas_por_usuario(request.user)
    filasPorUsuario = filaCarrito.objects.get_tareas_por_usuario(usuarioActivo)
    context['totalDefinitivo'] = 0
    for f in filasPorUsuario:
        context['totalDefinitivo'] += f.costoTarea    





    return render(request,'home/home.html',context)






def writeAndReadJson(nameAplication,option,ruta='static/json/historial.json'):
    """
    La función "writeAndReadJson" lee el archivo historial.json
    y lo guarda en la variable historial. 
    Posteriormente historial, que es un diccionario python,
    agrega una nueva key nameAplication con su respectivo
    valor option y lo agrega a historial.json.
    Retorna la variable historial.

    En el caso de que option sea un string vacío, sólo
    lee el archivo historial.json y lo retorna como 
    un diccionario python.

    La utilidad de esta función es generar el historial
    en el panel izquierdo de la plataforma, de tal modo
    que se genere a medida que se vaya avanzando, pero 
    que no se borre al retroceder.
    """
    import json

    if option != '':

        with open(ruta,'r') as f:
            historial = json.load(f)

        historial[nameAplication] = option

        with open(ruta,'w') as f:
            json.dump(historial,f)

    else:
        with open(ruta,'r') as f:
            historial = json.load(f)

    return historial



def readJson(ruta='static/json/carrito/carrito.json'):
    """
    readJson lee la información de un archivo de tipo
    diccionario .json, lo combierte a un diccionario
    tipo python y lo retorna.
    """
    import json

    with open(ruta,'r') as f:
        carrito = json.load(f)

    titulos = list(carrito.keys())
    totales = list(carrito.values())
    totalDefinitivo = sum(totales)

    tabla = []
    for i in range(len(carrito)):
        tabla.append(
            {
                'titulo':titulos[i],
                'total':totales[i]
            }
        )

    return tabla, totalDefinitivo




class usuariosListView(ListView):
    template_name = "home/usuario.html"
    context_object_name = "usuarios"
    paginate_by = 4
    

    def get_queryset(self):

        usuarios = User.objects.filter(
            is_staff = False
        ).order_by('primerApellido')

        return usuarios

    def get(self,request,*args, **kwargs):

        """
        Un usuario no identificado no puede acceder.
        """
        if not request.user.is_authenticated:
            return redirect('login_app:login')
        """
        Un usuario sin permisos de administrador no puede acceder
        """
        if not request.user.is_admin:
            return redirect('home_app:home')


        return super(usuariosListView,self).get(request, *args, **kwargs)


class eliminarUsuarioDetailView(DeleteView):
    model = User
    template_name = "home/eliminar_usuario.html"
    success_url = reverse_lazy("home_app:usuarios")
    context_object_name = "usuario"

    def get(self,request,*args, **kwargs):

        """
        Un usuario no identificado no puede acceder.
        """
        if not request.user.is_authenticated:
            return redirect('login_app:login')
        """
        Un usuario sin permisos de administrador no puede acceder
        """
        if not request.user.is_admin:
            return redirect('home_app:home')


        return super(eliminarUsuarioDetailView,self).get(request, *args, **kwargs)



class usuarioUpdateView(UpdateView):
    model = User
    template_name = "home/editar_usuario.html"
    success_url = reverse_lazy("home_app:usuarios")
    context_object_name = "usuario"
    fields = [
        'is_admin',
        'is_active'
    ]

    def get(self,request,*args, **kwargs):

        """
        Un usuario no identificado no puede acceder.
        """
        if not request.user.is_authenticated:
            return redirect('login_app:login')
        """
        Un usuario sin permisos de administrador no puede acceder
        """
        if not request.user.is_admin:
            return redirect('home_app:home')


        return super(usuarioUpdateView,self).get(request, *args, **kwargs)
