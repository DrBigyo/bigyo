from django.core.management.base import BaseCommand, CommandError
from loguru import logger


class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        logger.info('[Development] Entered a custom DAMHYEOK command for development 😎')

        from polls.models import reporter, Article
        for rep in reporter.objects.all().values():
            print(rep)

        r = reporter(full_name = 'John Smith')

        print('Done')
