from django.db import models

# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=15, null=False, blank=False, default='ACTIVO')
    created_at = models.DateTimeField('Fecha de Creación',auto_now=False, auto_now_add=True, null=False)
    updated_at = models.DateTimeField('Fecha de Actualización', auto_now=True, auto_now_add=False, null=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'