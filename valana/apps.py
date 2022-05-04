from email.policy import default
from django.apps import AppConfig


class ValanaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'valana'
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
