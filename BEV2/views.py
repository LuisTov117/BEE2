from django.shortcuts import render
from rest_framework import viewsets
from .Serializers import AlumnosSerializer,ProyectoSerializer,EmpresaSerializer,ConvocatoriaSerializer,Al_Conv_ProySerializer
from .models import Alumnos,Proyecto,Empresa,Convocatoria,Alumno_Cov_Proy
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import CreateView

import logging
# Create your views here.
class AlumnosView(viewsets.ModelViewSet):
    serializer_class = AlumnosSerializer
    queryset = Alumnos.objects.all()
    
    def perform_create(self, serializer):
        
        password = self.request.data.get('password')
        if password:
            
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

class EmpresaView(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    
    def perform_create(self, serializer):
        
        password = self.request.data.get('password')
        if password:
            
            serializer.validated_data['password'] = make_password(password)
        serializer.save()
        
class ConvocatoriaView(viewsets.ModelViewSet):
    serializer_class = ConvocatoriaSerializer
    queryset = Convocatoria.objects.all()
    
class ProyectoView(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()

class AlConvProyView(viewsets.ModelViewSet):
    serializer_class = Al_Conv_ProySerializer
    queryset = Alumno_Cov_Proy.objects.all()
  

class AlumnosLoginView(APIView):
    
    def post(self, request):
        
        matricula = request.data.get('matricula')
        password = request.data.get('password')
        
        try:
            
            alumno = Alumnos.objects.get(matricula=matricula)
            if check_password(password, alumno.password):
                
                return Response({'message': 'Autenticacion exitosa'})
        except Alumnos.DoesNotExist:
            pass
        
        return Response({'message': 'Error de autenticacion'}, status=401)
    

class EmpresaLoginView(APIView):
    
    def post(self, request):
        
        usuarioE = request.data.get('user')
        password = request.data.get('password')
        
        try:
            
            empresa = Empresa.objects.get(usuarioE=usuarioE)
            if check_password(password, empresa.password):
                
                return Response({'message': 'Autenticacion exitosa'})
        except Empresa.DoesNotExist:
            pass
        
        return Response({'message': 'Error de autenticacion'}, status=401)
    




    