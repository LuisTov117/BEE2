from django.contrib import admin
from .models import Alumnos,Empresa,Convocatoria,Alumno_Cov_Proy,Proyecto
# Register your models here.
admin.site.register(Alumnos)
admin.site.register(Empresa)
admin.site.register(Convocatoria)
admin.site.register(Proyecto)
admin.site.register(Alumno_Cov_Proy)
