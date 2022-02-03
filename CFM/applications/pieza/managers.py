from django.db import models


class TareaManager(models.Manager):
    
    def tareas_por_seccion(self,nombre_seccion):

        tareas_filtro = self.filter(
            seccion__nombre = nombre_seccion
        )

        return tareas_filtro

    def tareas_por_descripcion(self,descripcion,nombre_seccion):
        
        tareas_filtro = self.get(
            descripcion = descripcion,
            seccion__nombre = nombre_seccion
        )

        return tareas_filtro


    
class SubTareaManager(models.Manager):

    def subtareas_por_tareas(self,nombre_seccion):

        subtareas_filtro = self.filter(
            Tarea__seccion__nombre = nombre_seccion
        )

        return subtareas_filtro

    def subtareas_por_tarea(self,tarea):

        subtareas_filtro = self.filter(
            Tarea = tarea,
        )

        return subtareas_filtro

    def subtareas_por_descripcion(self,descripcion):

        subtareas_filtro = self.filter(
            descripcion = descripcion
        )

        return subtareas_filtro



class filaCarritoManager(models.Manager):

    def tareas_por_usuario(self,user):

        tareas_filtro = self.filter(
            User = user
        )
    
        return tareas_filtro 

    def get_tareas_por_usuario(self,user):

        tareas_filtro = self.filter(
            User = user
        )

        return tareas_filtro

    def fila_segun_descripcion(self,descripcion,id,user):
        fila_filtro = self.filter(
            Tarea__descripcion = descripcion,
            User = user,
            id_fila = id
        )
        
        return fila_filtro