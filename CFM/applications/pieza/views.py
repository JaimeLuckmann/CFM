from django.views.generic import ListView
from .models import Tarea , SubTarea , filaCarrito
from applications.seccion.models import Seccion
from django.shortcuts import render, redirect
from applications.home.views import writeAndReadJson
from django.urls import reverse_lazy, reverse

def pieza(request):

    usuarioActivo = request.user 

    """
    Esto impide que un usuario no registrado 
    pueda acceder a las páginas
    """
    if not request.user.is_authenticated:
        return redirect('login_app:login')




    """
    Diccionario que conecta los nombres de las secciones de 
    la base de datos con los nombres de los archivos .html:
    """

    Dict_secciones = {
        'CuchilloIzquierdo':'cuchillo_izquierdo.html',
        'CuchilloDerecho':'cuchillo_derecho.html',
        'RodilloLateral':'Rodillo_lateral.html',
        'LinkRodillo':'link_rodillo.html',
        'LinkCuchillo':'link_cuchillo.html',
        'CuchilloFlotante':'cuchillo_flotante.html',
        'BrazoRodillo':'brazo_rodillo.html',
        'Articulacion':'articulacion.html',
        'Chasis':'chasis.html',
        'TapaCabezal':'tapa_cabezal.html',
        'RodilloCentral1':'rodillo_central_1.html',
        'CilindroVolteo':'cilindro_volteo.html',
        'CilindroBrazos':'cilindro_brazos.html',
        'CilindroCuchillo':'cilindro_cuchillo.html',
        'CilindroMedicion':'cilindro_medicion.html',
        'PasadoresCuchillo':'pasadores_cuchillo.html',
        'PasadorRodillo':'pasador_rodillo.html',
    }



    """
    El diccionario "options" crea una biyección entre la señal
    mandada desde el html y el string que se muestra en el 
    panel izquierdo.
    """
    options = {
        'CuchilloIzquierdo':'Cuchillo izquierdo',
        'CuchilloDerecho':'Cuchillo derecho',
        'RodilloLateral':'Rodillo lateral',
        'LinkRodillo':'Link rodillo',
        'LinkCuchillo':'Link cuchillo',
        'CuchilloFlotante':'Cuchillo flotante',
        'BrazoRodillo':'Brazo rodillo',
        'Articulacion':'Articulación',
        'Chasis':'Chasis',
        'TapaCabezal':'Tapa cabezal',
        'RodilloCentral1':'Rodillo central 1',
        'CilindroVolteo':'Cilindro volteo',
        'CilindroBrazos':'Cilindro brazos',
        'CilindroCuchillo':'Cilindro cuchillo',
        'CilindroMedicion':'Cilindro medición',
        'PasadoresCuchillo':'Pasadores de cuchillo',
        'PasadorRodillo':'Pasador de rodillo',
    }

    inv_options = {v: k for k, v in options.items()}

    pieza = request.GET.get('pieza',)
    """
    Cambiar repeticiones y precio de subtareas dentro de una tarea seleccionada:
    """
    tareaModificar = request.GET.get('modificar',)
    if tareaModificar:
        nombre_seccion = options[pieza]
        tareaObjeto = Tarea.objects.tareas_por_descripcion(tareaModificar,nombre_seccion)
        subtareasModificar = SubTarea.objects.subtareas_por_tarea(tareaObjeto)
        for subtarea in subtareasModificar:
            repeticiones = request.GET.get('repeticiones '+subtarea.descripcion,)
            repeticiones = repeticiones.replace(",",".")
            
            costo = filter(str.isdigit, request.GET.get('costo '+ subtarea.descripcion,))
            costo = "".join(costo)
            SubTarea.objects.subtareas_por_descripcion(
                subtarea.descripcion
                ).update(
                    costo=costo,
                    repeticiones=repeticiones
                    )

            
            

    context = {}
    


    """
    Eliminar fila del carrito
    """
    eliminarFila = request.GET.get('eliminar','')
    id_eliminar = request.GET.get('id-eliminar','')
    if len(eliminarFila)>0:
        filaBorrar = filaCarrito.objects.fila_segun_descripcion(eliminarFila,id_eliminar,usuarioActivo)
        tarea_id = list(filaBorrar.values())[0]['Tarea_id']
        seccion_volver = list(Tarea.objects.filter(
            descripcion = eliminarFila,
            id_tarea = tarea_id,
        ).values('seccion__nombre'))[0]['seccion__nombre']



        filaBorrar.delete()
        return redirect(reverse('pieza_app:pieza')+"?pieza=%s" % inv_options[seccion_volver])

    context = ListaSubTarea(options[pieza])


    """
    Carrito:
    """

    
    """
    Mostrar información en el carrito
    """
    seccion_elegida = request.GET.get("pieza",'')
    historial = writeAndReadJson('seccion',options[seccion_elegida])
    
    context['historial'] = historial

    

    """
    Si se agrega una tarea se añade a la tabla filaCarrito en la base de datos.
    """
    tareaAgregada = request.GET.get('agregar','')

    if tareaAgregada:
        #Agréga a la base de datos en tabla filaCarrito
        nombre_seccion = options[pieza]
        tareaObjeto = Tarea.objects.tareas_por_descripcion(tareaAgregada,nombre_seccion)
        tareaSeleccionada = Tarea(
            id_tarea = tareaObjeto.id_tarea,
            descripcion = tareaObjeto.descripcion,
            numero = tareaObjeto.numero,
            seccion = tareaObjeto.seccion
        )
        # listaSubtareas = [l for l in request.GET.keys() if l!='agregar' and l!='seccion' ]
        listaSubtareas = SubTarea.objects.subtareas_por_tarea(
            tareaSeleccionada
            )
        preciosSubtareas = [subtarea.costo for subtarea in listaSubtareas]
        preciosSubtareas = []
        for subtarea in listaSubtareas:
            repeticiones = float(request.GET.get('repeticiones '+subtarea.descripcion,))

            # repeticiones = float(repeticiones.replace(",","."))
            preciosSubtareas.append(subtarea.costo*repeticiones)

        precioTarea = sum(preciosSubtareas)

        filaCarrito.objects.create(
            User = usuarioActivo,
            Tarea = tareaSeleccionada,
            costoTarea = precioTarea
        ).save()


    filasPorUsuario = filaCarrito.objects.get_tareas_por_usuario(usuarioActivo)
    context['totalDefinitivo'] = 0
    for f in filasPorUsuario:
        context['totalDefinitivo'] += f.costoTarea

    """
    Realiza una petición a la tabla filaCarrito en la base de datos y
    retorna todas las tareas con sus respectivos precios filtrando
    por el usuario que tenga la sesión activa para que al cerrar sesión
    o cambiar de usuario no pierda su cotización.
    """
    context['fila'] = filaCarrito.objects.tareas_por_usuario(request.user)


    """
    ¿Es administrador?
    """
    if request.user.is_admin:
        context['admin'] = 'admin'


    return render(request,'pieza/'+Dict_secciones[pieza],context)



def ListaSubTarea(seccion):
    """
    la variable lst debe ser modificada. El objetivo sería hacer un llamado a la base de datos,
    primero filtrando por cuales serían las tareas para una sección en particular y luego
    cuales son las subtareas correspondientes a esas tareas. 
    Por el momento lo dejaré así.

    update: logré hacerlo con slst.
    update: logré hacerlo también con slst.
    """
    lst = Tarea.objects.tareas_por_seccion(seccion)

    slst = SubTarea.objects.subtareas_por_tareas(seccion)

    data = {
        'lst': lst,
        'slst': slst
    }

    return data