import urllib.request as urllib
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand
from ...models import Currency


class Command(BaseCommand):
    help = 'Updates exchange rates at current rate of BNB'

    def handle(self, *args, **options):
        url = 'http://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm?download=xml&search=&lang=BG'
        file = urllib.urlopen(url)
        data = file.read()
        file.close()

        tree = ET.ElementTree(ET.fromstring(data))
        root = tree.getroot()
        iterrows = iter(root.findall('ROW'))
        next(iterrows)
        for row in iterrows:
            import ipdb; ipdb.set_trace()
            currency = row.find('CODE').text
            course = row.find('RATIO').text

            updates = {'currency': currency, 'course': course}
            currency, created = Currency.objects.update_or_create(
                                                        currency=currency,
                                                        course=course,
                                                        defaults=updates)
            if created:
                self.stdout.write('{} was created'.format(currency))
            else:
                self.stdout.write('{} was updated'.format(currency))