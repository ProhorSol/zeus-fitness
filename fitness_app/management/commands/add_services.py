from django.core.management.base import BaseCommand
from fitness_app.models import Service

class Command(BaseCommand):
    help = 'Adds default services'

    def handle(self, *args, **options):
        services = [
            {
                'title': 'Аэробика',
                'description': 'Гимнастика, состоящая из аэробных упражнений под ритмичную музыку, которая помогает следить за ритмом выполнения упражнений',
                'icon': 'fa fa-futbol-o',
                'order': 1
            },
            {
                'title': 'Кардио',
                'description': 'Это вид физических нагрузок, который способствует повышению пульса в определенных рамках, повышает кровообращение',
                'icon': 'fa fa-compass',
                'order': 2
            },
            {
                'title': 'Cycle-тренировки',
                'description': 'Сайкл-тренировки представлены программами Rider и Rider X для новичков, искушенных атлетов, желающих поддерживать форму',
                'icon': 'fa fa-database',
                'order': 3
            },
            {
                'title': 'GymTime Full Body',
                'description': 'Комплексная тренировка в тренажерном зале, включает в себя упражнения на все основные группы мышц: спины, ягодиц, ног и кора',
                'icon': 'fa fa-bar-chart',
                'order': 4
            },
            {
                'title': 'BootyBlaster',
                'description': 'Способствует развитию мышц ног и делает ягодицы более упругими и подтянутыми. Способствует развитию мышц ног',
                'icon': 'fa fa-paper-plane-o',
                'order': 5
            },
            {
                'title': 'Йога',
                'description': 'Позволит выстроить правильную, гармоничную работу всех систем и органов тела, включить в работу дыхание, концентрацию',
                'icon': 'fa fa-bullseye',
                'order': 6
            },
        ]

        for service_data in services:
            Service.objects.get_or_create(
                title=service_data['title'],
                defaults={
                    'description': service_data['description'],
                    'icon': service_data['icon'],
                    'order': service_data['order'],
                    'is_active': True
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added service "{service_data["title"]}"'))
