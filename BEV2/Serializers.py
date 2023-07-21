from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Alumnos,Empresa,Convocatoria,Alumno_Cov_Proy,Proyecto

userModel = get_user_model()

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'
        
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
class ConvocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocatoria
        fields = '__all__'
        
class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        
class Al_Conv_ProySerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno_Cov_Proy
        fields = '__all__'
        

