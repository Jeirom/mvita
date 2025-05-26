from django.core.management import BaseCommand

from mvita_main.models import Doctors


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Doctors"

    def handle(self, *args, **kwargs):
        # Пример добавления одного объекта
        my_instance = Doctors(
            first_name="Иван",
            last_name="Иванов",
            specialization="Директор, врач-диагност",
            experience="22 года",
        )
        my_instance.save()
        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
