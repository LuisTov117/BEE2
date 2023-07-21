from django.db import models
import argon2


# Create your models here.
class Alumnos(models.Model):
    matricula = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=50)
    apellidoM = models.CharField(max_length=50)
    carrera = models.CharField(max_length=80, default='')
    sexo = models.CharField(max_length=1)
    correo = models.CharField(max_length=30)
    usuario = models.CharField(max_length=6)
    password = models.CharField(max_length=200, default=" ")
    
    def __str__(self) -> str:
        return self.matricula
    
    def set_password(self, raw_password):
        
        hasher = argon2.PasswordHasher()
        self.password = hasher.hash(raw_password)
        
    def check_password(self, raw_password):
        
        hasher = argon2.PasswordHasher()
        
        try:
            hasher.verify(self.password, raw_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False
    
    
class Empresa(models.Model):
    id_empresa = models.CharField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50)
    nomb_enlace = models.CharField(max_length=50)
    titular = models.CharField(max_length=80)
    cargo_titular = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    usuarioE = models.CharField(max_length=6)
    password = models.CharField(max_length=200, default=" ")
    
    def __str__(self)-> str:
        return self.nombre_empresa
    
    
    def set_password(self, raw_password):
        
        hasher = argon2.PasswordHasher()
        self.password = hasher.hash(raw_password)
        
    def check_password(self, raw_password):
        
        hasher = argon2.PasswordHasher()
        
        try:
            hasher.verify(self.password, raw_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False

    
class Convocatoria(models.Model):
    id_conv = models.IntegerField(primary_key = True)
    periodo = models.CharField(max_length=30)
    proceso = models.CharField(max_length=50)
    año = models.DateField
    
    def __str__(self)-> str:
        return self.proceso
    
class Proyecto(models.Model):
    id_empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)
    cns_proyecto = models.IntegerField
    nomb_proy = models.CharField(max_length = 80)
    modalidad = models.CharField(max_length = 50)
    asesor = models.CharField(max_length = 80)
    carrera = models.CharField(max_length = 100)
    justificacion = models.CharField(max_length=300, default='')
    objetivo = models.CharField(max_length=300, default='')
    
class Alumno_Cov_Proy(models.Model):
    id_alum = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    id_cov = models.ForeignKey(Convocatoria, on_delete=models.CASCADE)
    id_proy = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    estatus = models.CharField(max_length = 100)


    