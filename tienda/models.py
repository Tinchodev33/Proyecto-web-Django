from django.db import models

# Create your models here.

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    web = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Distribuidores"
        
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500, null=True)
    distribuidor = models.ForeignKey('distribuidor', on_delete=models.CASCADE)
    TIPO = [
        ('software', 'Software'),
        ('hardware', 'Hardware'), 
    ]
    tipo = models.CharField(max_length=8,choices=TIPO)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='imagenes')
    
    def __str__(self):
        return '%s %s' % (self.nombre, self.tipo)
 
opciones_consultas = [
     [0, 'Consulta'],
     [1, 'Reclamo'],
     [2, 'Envios'],
     [3, 'Calificación']
]
 
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField(max_length=150)
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre