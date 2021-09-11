from django.db import models

# Create your models here.
class Cliente(models.Model):
    doc = ( 
        ('D', 'DPI'),
        ('C', 'CEDULA'),
    )
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=50)
    nacimiento =models.DateField()
    tipo = models.ForeignKey(
        'TipoCliente',
        on_delete= models.CASCADE,
        default=1
    )
    documento =models.CharField(
        max_length=20,
        choices=doc,
        default='C'
    )
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class TipoCliente(models.Model):
    tipo =models.CharField(max_length=50)
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.tipo)

class Ventas(models.Model):
    cliente =models.ManyToManyField(Cliente)
    fecha =models.DateTimeField()

class estudiante(models.Model):
    nombre =models.CharField(max_length=50)
    direccion =models.CharField(max_length=50)
    carne =models.CharField(max_length=50)
    grado = models.ForeignKey(
        'Grados',
        on_delete= models.CASCADE,
        default=1
    )

    def __str__(self):
        return '%s' % (self.nombre)

class docente(models.Model):
    nombre =models.CharField(max_length=50)
    direccion =models.CharField(max_length=50)
    Curso =models.CharField(max_length=50)
    Docente_de = models.ForeignKey(
        'Grados',
        on_delete= models.CASCADE,
        default=1
    )

    def __str__(self):
        return '%s' % (self.nombre)

class Grados(models.Model):
    grado =models.CharField(max_length=50)
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)
    

    def __str__(self):
        return '%s' % (self.grado)

class AcercaDe(models.Model):
    Te_Contactamos=models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.Te_Contactamos)
