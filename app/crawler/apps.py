from django.apps import AppConfig


class CrawlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crawler'

    def ready(self):
        print('yo man')
