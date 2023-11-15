from django.db import models

# Create your models here.

TIPO_IVA_CHOICE = (
    ("CF", "Consumidor final"),
    ("RI", "Responsable Inscripto"),
    ("MT", "Monotributo")
)


class Localidad(models.Model):
    nombre = models.CharField("Nombre de la localidad", max_length=50)
    cp = models.CharField("Cód. postal", max_length=10)
    provincia = models.CharField(max_length=50)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField("Nombre/s", max_length=120)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_nac = models.DateField("Fecha de nacimiento", null=True, blank=True)
    tipo_iva = models.CharField("Tipo de IVA", max_length=2, choices=TIPO_IVA_CHOICE, default="CF")
    # total = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)


# Modelo.objects.create() ->  Insertar un dato
# Modelo.objects.all() -> Retorna todos los objetos de la tabla
# Modelo.objects.get(nombre_campo=valor) Retorna el registro que cumpla con la condicion
# Modelo.objects.filter(nombre_campo__*) Retorna un conjunto de datos que coincidan con el argumento
# CAMPOS NUMERICOS
# * gt (mayor que)
# * gte (mayor o igual a)
# * lt (menor que)
# * lte (menor o igual que)
# * = (igual al parametro)
# CAMPOS DE TEXTO
# contains
# startswith
# endswith
