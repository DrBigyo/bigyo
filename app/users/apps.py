from django.apps import AppConfig
from loguru import logger


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


    def ready(self):
        from .models import User

        try:
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(name='admin', password='drbpw12!@')
                logger.info('[User] Admin "admin" account created ✅')
        except Exception as e:
            pass