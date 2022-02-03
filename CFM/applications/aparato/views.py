from django.shortcuts import render, redirect
from applications.home.views import writeAndReadJson, readJson
from applications.pieza.models import filaCarrito


def aparato(request):

    usuarioActivo = request.user 


    """
    Esto impide que un usuario no registrado 
    pueda acceder a las páginas
    """
    if not request.user.is_authenticated:
        return redirect('login_app:login')

    """
    la variable "home" obtiene desde el archivo home.html
    la opción según selecciona el usuario desde la página.
    """
    home = request.GET.get("home",'')

    """ 
    El diccionario "options" crea una biyección entre la señal
    mandada desde el html y el string que se muestra en el 
    panel izquierdo.
    """
    options = {
        'hacerCotizacion': 'Hacer cotización',
        'cambiarCosto': 'Cambiar costo',
        '':''
    }

    """
    La siguiente línea añade al archivo historial.json la 
    clave 'home' con su valor respectivo options[home].
    """
    historial = writeAndReadJson('home',options[home])

    """
    El archivo "context" es devuelto a base.html para que se 
    agregue o actualice el historial en el panel izquierdo.
    """
    context = {}
    context['historial'] = historial


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

    


    return render(request,'aparato/aparato.html',context)

