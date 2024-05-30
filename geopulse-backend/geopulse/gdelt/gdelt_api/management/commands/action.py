from django.core.management.base import BaseCommand
from django.utils import timezone
from geopulse.gdelt.gdelt_api.gdelt_api import GdeltAPI
from geopulse.gdelt.gdelt_api.utils.url_util import UrlUtils as _url
class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        print(_url.construct_default_url())
