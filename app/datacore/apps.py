from django.apps import AppConfig


class DatacoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'datacore'


    def ready(self):
        print('Datacore initialization here')