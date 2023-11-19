from django.core.management.base import BaseCommand, CommandError
from loguru import logger


class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        logger.info('[Development] Entered a custom DAMHYEOK command for development 😎')
