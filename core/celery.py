#Activamos los imports absolutos para evitar conflictos entre packages
import os
from celery import Celery

# Establecer la configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Crea una instancia de la aplicación Celery
app = Celery('core')

# Lee la configuración de Celery desde la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre y registra automáticamente las tareas en tu aplicación Django
app.autodiscover_tasks()
