from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator
from .managers import TareaManager, SubTareaManager, filaCarritoManager
from applications.seccion.models import Seccion
from applications.login.models import User
#Managers
from .managers import TareaManager

"""
Define el modelo relacional "Tarea" en la base de datos.

Cada Tarea debe pertenecer a una cierta sección.
Una sección puede tener distintas tareas.
Una tarea incluye un grupo de subtareas.

Las tareas son el string que le interesa finalmente al usuario.
"""
class Tarea(models.Model):
    """  """
    id_tarea = models.BigAutoField(primary_key=True)
    descripcion = models.CharField('descripción de la tarea',max_length=70)
    numero = models.PositiveIntegerField('número de la tarea según imágen',null=True)

    seccion = models.ForeignKey(
        Seccion,
        on_delete=CASCADE,
        null=True,
        related_name='subtarea_tarea'
    )

    objects = TareaManager()

    def __str__(self):
        return str(self.id_tarea) + '-' + self.descripcion


""" 
Define el modelo relacional "Subtarea" en la base de datos.

Cada Subtarea pertenece a una tarea particular.
Cada Subtarea tiene un precio asociado con una cantidad 
de repeticiones asociada. Las repeticiones representan la
cantidad de HH o de gastos de material que se efectuaron
para realizar tal Subtarea.

El conjunto de Subtareas con sus repeticiones será 
posteriormente sumado a un total que le corresponderá 
a la tarea en cuestión y será pasado al "carrito de compra".
"""
class SubTarea(models.Model):
    #Atributos
    id_subtarea = models.BigAutoField(primary_key=True)
    descripcion = models.CharField('Material o tarea',max_length=70)
    costo = models.PositiveIntegerField('Costo')
    repeticiones = models.DecimalField(
            max_digits=6,
            decimal_places=2,
            validators=[MinValueValidator(0.01)],
            null=True
        )
    
    #Clave foránea:
    Tarea = models.ForeignKey(Tarea,on_delete=CASCADE)

    objects = SubTareaManager()

    def __str__(self):
        return  str(self.id_subtarea) + '-' + self.descripcion +' ('+ self.Tarea.descripcion+')'

    @property
    def costo_dot_repeticiones(self):
        return round(self.costo * self.repeticiones)

class filaCarrito(models.Model):
    #Atributos
    id_fila = models.BigAutoField(primary_key=True)
    User = models.ForeignKey(User,on_delete=CASCADE)
    Tarea = models.ForeignKey(
        Tarea,
        on_delete=CASCADE,
        related_name='filaCarrito_tarea')
    costoTarea = models.PositiveIntegerField('Costo Tarea')

    objects = filaCarritoManager()

    def __str__(self):
        return str(self.User) + ' - ' + str(self.Tarea) 