from django.core.management.base import BaseCommand, CommandError
from shortener.models import shortitURL

class Command(BaseCommand):
    help = 'Refreshes all Url shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return shortitURL.objects.refresh_shortcodes(items=options['items'])
