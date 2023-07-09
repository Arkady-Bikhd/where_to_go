import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from ...models import Place, Image


class Command(BaseCommand):
    help = 'Загрузка данных из файлов'

    def add_arguments(self, parser) -> None:
        parser.add_argument('url', type=str, help='адрес файла данных в формате json')

    def handle(self, *args, **options) -> str | None:
        json_file_url = options['url']
        response = requests.get(json_file_url)
        response.raise_for_status()
        place_params = response.json()
        try:
            title = place_params['title']
            description_short = place_params.get(['description_short'], '')
            description_long = place_params.get(['description_long'], '')
            latitude = place_params['coordinates']['lat']
            longitude = place_params['coordinates']['lng']
            image_urls = place_params.get(['imgs'], [])
        except KeyError:
            print('Файл содержит неполные данные')
            return
        try:
            place, created = Place.objects.get_or_create(
                title=title,
                defaults={
                    description_short: description_short,
                    description_long: description_long,
                    latitude: latitude,
                    longitude: longitude,
                }
            )            
            if created:
                save_place_image(place, image_urls)
                print(f'Объект {title} с соответствующими изображениями создан')
        except Place.MultipleObjectsReturned:
            print('В базе данных найдено несколько записей')


def save_place_image(place, image_urls) -> None:
    for number, image_url in enumerate(image_urls):
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        image_file = ContentFile(
            image_response.content,
            name=f'{title}_{number}.jpg'
        )
        Image.objects.create(
            place=place,
            image=image_file,
            image_number=number
        )
