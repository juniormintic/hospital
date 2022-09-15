from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Rol)
admin.site.register(Personal_medico)
admin.site.register(Familiar)
admin.site.register(Historico)
admin.site.register(Sugerencias)
admin.site.register(SignosVitales)
admin.site.register(Auxiliar)


