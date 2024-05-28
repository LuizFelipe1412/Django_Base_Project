from django.apps import AppConfig
from core.settings import PROJECT_NAME_SUFFIX


class SigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sig'
    verbose_name = f"Sistema Integrado de Gestão  :: {PROJECT_NAME_SUFFIX}"
