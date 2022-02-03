from django.contrib import admin
from .models import User



class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'nombre',
        'primerApellido'
    )

admin.site.register(User,UserAdmin)