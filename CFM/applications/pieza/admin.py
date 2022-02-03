from django.contrib import admin
from .models import Tarea, SubTarea, filaCarrito

#Las siguientes clases estilizan la interfaz del admin de django
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        'seccion',
        'numero',
        'descripcion',
    )

class SubTareaAdmin(admin.ModelAdmin):
    list_display = (
        'Tarea',
        'id_subtarea',
        'descripcion',
        'costo'
    )

class filaCarritoAdmin(admin.ModelAdmin):
    list_display = (
        'Tarea',
        'costoTarea',
        'User'
    )


admin.site.register(Tarea,TareaAdmin)
admin.site.register(SubTarea,SubTareaAdmin)
admin.site.register(filaCarrito,filaCarritoAdmin)