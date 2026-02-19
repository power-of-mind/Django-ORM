import csv
from django.core.management.base import BaseCommand
from catalog.models import Phone


class Command(BaseCommand):
    help = 'Import phones'

    def handle(self, *args, **options):
        with open('phones.csv', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                Phone.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'name': row['name'],
                        'image': row['image'],
                        'price': row['price'],
                        'release_date': row['release_date'],
                        'lte_exists': row['lte_exists'] == 'True',
                    }
                )

        self.stdout.write(self.style.SUCCESS('Import completed'))