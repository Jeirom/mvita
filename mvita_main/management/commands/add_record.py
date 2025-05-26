from django.core.management import BaseCommand

from mvita_main.models import Record, Doctors, Services


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Record"

    def handle(self, *args, **kwargs):
        # Получаем объект Doctor с id=1
        try:
            doctor_instance = Doctors.objects.get(id=1)
        except Doctors.DoesNotExist:
            self.stdout.write(self.style.ERROR("Доктор с id=1 не найден."))
            return

        # Получаем объект Services с id=1
        try:
            services_instance = Services.objects.get(id=1)
        except Services.DoesNotExist:
            self.stdout.write(self.style.ERROR("Услуга с id=1 не найден."))
            return

        # Получаем объект User с id=1
        try:
            services_instance = Services.objects.get(id=1)
        except Services.DoesNotExist:
            self.stdout.write(self.style.ERROR("Услуга с id=1 не найден."))
            return

        my_instance = Record(
            doctor=doctor_instance,
            patient_name="Иванов",
            services=services_instance,
            addres="Улица Здоровья",
        )
        my_instance.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
