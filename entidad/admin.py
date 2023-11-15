from django.contrib import admin
from .import models

# Register your models here.

my_models = [models.Localidad, models.Persona]

admin.site.register(my_models)