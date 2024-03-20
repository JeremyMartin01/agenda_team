from django.contrib import admin
from .models import Person, Hobby, Reunion

#Es importante registrar los modelos, para que esten disponibles el módulo de administrador y aplicar 
admin.site.register(Person)
admin.site.register(Hobby)
admin.site.register(Reunion)