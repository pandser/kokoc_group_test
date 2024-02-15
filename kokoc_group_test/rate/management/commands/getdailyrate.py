import requests
import time

from django.core.management.base import BaseCommand
from rate.constants import NUM_RETRIES, TIME_RETRIES,URL_SOURCE_RATE
from rate.models import Valute


class Command(BaseCommand):

    def handle(self, *args, **options):
        responce = None
        for _ in range(NUM_RETRIES):
            try:
                responce = requests.get(URL_SOURCE_RATE)
                break
            except requests.exceptions.ConnectionError:
                time.sleep(TIME_RETRIES)
                continue
        if responce:
            data = []
            for k, v in responce.json().get('Valute').items():
                data.append(Valute(
                                date=responce.json().get('Date').split("T")[0],
                                name=v.get('Name'),
                                charcode=k,
                                rate=v.get('Value') / v.get('Nominal'),
                            ))
            Valute.objects.bulk_create(data)
        else:
            return 'ConnectionError'
