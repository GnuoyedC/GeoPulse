from django.core.management.base import BaseCommand
from django.utils import timezone
import geopulse.gdelt.geopulse_gdelt.processing.csv_processor as csvprocs
from geopulse.gdelt.geopulse_gdelt.geopulse_gdelt import GeopulseGDELTHandler
class Command(BaseCommand):
    help = 'Displays current time'
    
    def handle(self, *args, **kwargs):
        #csvprocs.cfg.get_codes_config()
        GeopulseGDELTHandler.test()
