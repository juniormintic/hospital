from django.db import models

# Create your models here.
class Rol(models.Model):
    codigo_rol=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=45)
    valores=[
        ('on','Activo'),
        ('off','Inactivo')
    ]
    activo=models.CharField(max_length=3, choices=valores,default="on")

    def __str__(self):
        txt= "{0} {1} {2}"
        return txt.format(self.codigo_rol, self.nombre,self.activo)

class Persona(models.Model):
    identificacion=models.CharField(max_length=10,primary_key=True)
    tiposDocumentos=[
        ('CC','Cedula'),
        ('TI','Tarjeta Identidad')
    ]
    tipo_documento=models.CharField(max_length=2, choices=tiposDocumentos,default="CC")
    nombre=models.CharField(max_length=45 )
    apellido=models.CharField(max_length=45)
    fecha_nacimiento=models.DateField()
    sexos=[
        ('F','Femenino'),
        ('M','Masculino')
    ]
    sexo=models.CharField(max_length=1, choices=sexos, default='F')

    email=models.EmailField(max_length=45, unique=True)    
    #cambiar tipo de dato de telefono
    telefono=models.CharField(max_length=10)
    direccion=models.CharField(max_length=45)
    ciudad=models.CharField(max_length=45)
    ##Ver si se puede Automatico
    fecha_registro=models.DateField()
    codigo_rol=models.ForeignKey(Rol,null=False, blank=False, on_delete=models.CASCADE)
    ##Cambiar tipo pass
    password= models.CharField( max_length=45)
    def nombrecompleto(self):
        txt="{0} {1}"
        return txt.format(self.apellido,self.nombre)
    def __str__(self):
        txt="{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}"
        return txt.format(self.tipo_documento,self.identificacion,self.nombrecompleto(),self.fecha_nacimiento,self.sexo,self.email,self.telefono,self.direccion,self.ciudad,self.codigo_rol,self.password)

class Auxiliar(models.Model):
    cargo=models.CharField(max_length=45)
    fecha_contrato=models.DateField()
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        txt="{0} {1} {2}"
        return txt.format(self.cargo,self.fecha_contrato,self.identificacion)

class Familiar(models.Model):
    parentesco=models.CharField(max_length=45,null=False)
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        txt="{0} {1}"
        ##Observacion para nombre completo
        return txt.format(self.identificacion,self.parentesco)

class Personal_medico(models.Model):
    anio_contrato=models.IntegerField()
    especialidad=models.CharField(max_length=30,null=False)
    area=models.CharField(max_length=30)
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        txt="{0} {1} {2}"
        return txt.format(self.area,self.identificacion,self.especialidad)

class Paciente(models.Model):
    georreferencia= models.CharField( max_length=45)
    especialidad_doctor= models.CharField( max_length=30)
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        txt="{0} {1} {2}"
        return txt.format(self.identificacion,self.especialidad_doctor,self.georreferencia)

class Sugerencias(models.Model):
    id_codigo=models.PositiveIntegerField(primary_key=True)
    diagnostico=models.CharField( max_length=45)
    recomendaciones=models.CharField( max_length=45)
    fecha=models.DateField()
    doctor=models.ForeignKey(Personal_medico,null=False, blank=False, on_delete=models.CASCADE)
    historico=models.ForeignKey(Paciente,null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        txt="{0} {1} {2} {3}"
        return txt.format(self.id_codigo,self.doctor,self.fecha,self.diagnostico,self.recomendaciones)

class Historico(models.Model):
    paciente=models.OneToOneField(Paciente,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    codigo=models.PositiveIntegerField()
    valores=[
        ('Si','Si'),
        ('No','No')
    ]
    en_cuidado=models.CharField(max_length=3, choices=valores,default="Si")
    def __str__(self):
        txt="{0} {1} {2}"
        return txt.format(self.codigo,self.paciente,self.en_cuidado)

class SignosVitales(models.Model):
    id_codigo=models.AutoField(primary_key=True)
    oximetria=models.CharField( max_length=45)
    frecuencia_respiratoria=models.CharField( max_length=45)
    frecuencia_cardica=models.CharField( max_length=45)
    temperatura=models.CharField( max_length=45)
    presion_arterial=models.CharField( max_length=45)
    glicemia=models.CharField( max_length=45)
    fecha=models.DateField()
    historico=models.ForeignKey(Paciente,null=False, blank=False, on_delete=models.CASCADE)   
    #Revisar 
    historico_Paciente_Doctor_especialidad=models.CharField( max_length=30)
    codigo=models.ForeignKey(Historico,null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        txt="{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}"
        return txt.format(
            self.id_codigo,self.codigo,self.fecha,self.oximetria,self.frecuencia_respiratoria,
            self.frecuencia_respiratoria,self.frecuencia_cardica,self.temperatura,self.presion_arterial,
            self.glicemia,self.historico_Paciente_Doctor_especialidad)