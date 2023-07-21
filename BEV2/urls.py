from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from BEV2 import views
from .views import *

router = routers.DefaultRouter()
router.register(r'Alumnos',views.AlumnosView,'alumnos')
router.register(r'Empresas',views.EmpresaView,'empresas')
router.register(r'Proyectos',views.ProyectoView,'proyectos')
router.register(r'Convocatorias',views.ConvocatoriaView,'convocatorias')
router.register(r'AlConProy',views.AlConvProyView,'AlConProy')

urlpatterns = [
    path("api/", include(router.urls)),
    path("loginA/", AlumnosLoginView.as_view(), name= 'login'),
    path("loginE/", EmpresaLoginView.as_view(), name='login'),

]
