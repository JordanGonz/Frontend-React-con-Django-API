from django.db import models

# Create your models here.


class Admin1(models.Model):
    usuario = models.CharField(max_length=100)
    correo = models.EmailField((""), max_length=254)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=100, default='M')
    altura = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    peso = models.PositiveSmallIntegerField(default=0)
    correo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="paciente_fotos", null=True , blank=True)
    alergia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Cita de {self.paciente.nombre} con {self.medico.nombre} el {self.fecha}"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    costo = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
