from django.apps import AppConfig

from core.settings import PROJECT_NAME_SUFFIX

class DashConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dash'
    verbose_name = f"Dashboard  :: {PROJECT_NAME_SUFFIX}"
