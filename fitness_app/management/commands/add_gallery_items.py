from django.core.management.base import BaseCommand
from django.core.files import File
from fitness_app.models import Gallery
import os

class Command(BaseCommand):
    help = 'Adds default gallery items'

    def handle(self, *args, **options):
        gallery_items = [
            {
                'title': 'Тренажерный зал',
                'description': 'Современное оборудование для силовых тренировок',
                'image_path': 'static/images/portfolio/01.jpg',
                'category': 'gym',
                'order': 1
            },
            {
                'title': 'Йога-студия',
                'description': 'Просторный зал для занятий йогой',
                'image_path': 'static/images/portfolio/02.jpg',
                'category': 'yoga',
                'order': 2
            },
            {
                'title': 'Кардио-зона',
                'description': 'Беговые дорожки и велотренажеры',
                'image_path': 'static/images/portfolio/03.jpg',
                'category': 'cardio',
                'order': 3
            },
            {
                'title': 'Групповые занятия',
                'description': 'Зал для групповых тренировок',
                'image_path': 'static/images/portfolio/04.jpg',
                'category': 'group',
                'order': 4
            },
            {
                'title': 'Силовая зона',
                'description': 'Зона свободных весов',
                'image_path': 'static/images/portfolio/05.jpg',
                'category': 'gym',
                'order': 5
            },
            {
                'title': 'Растяжка',
                'description': 'Зона для растяжки и разминки',
                'image_path': 'static/images/portfolio/06.jpg',
                'category': 'yoga',
                'order': 6
            },
        ]

        for item_data in gallery_items:
            image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), item_data['image_path'])
            
            # Проверяем, существует ли уже такое изображение в галерее
            if not Gallery.objects.filter(title=item_data['title']).exists():
                with open(image_path, 'rb') as image_file:
                    gallery_item = Gallery(
                        title=item_data['title'],
                        description=item_data['description'],
                        category=item_data['category'],
                        order=item_data['order'],
                        is_active=True
                    )
                    # Сохраняем объект, чтобы получить ID
                    gallery_item.save()
                    
                    # Теперь добавляем изображение
                    gallery_item.image.save(
                        os.path.basename(image_path),
                        File(image_file)
                    )
                    
                    self.stdout.write(self.style.SUCCESS(f'Successfully added gallery item "{item_data["title"]}"'))
