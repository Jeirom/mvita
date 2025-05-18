from django.core.management import BaseCommand

from mvita_main.models import Record, DiagnosticResults


class Command(BaseCommand):
    help = "Добавляет данные в таблицу DiagnosticResults"

    def handle(self, *args, **kwargs):
        try:
            record_instance = Record.objects.get(id=4)
        except Record.DoesNotExist:
            self.stdout.write(self.style.ERROR("Запись с id=4 не найден."))
            return

        # Создайте новый объект DiagnosticResults
        diagnostic_result = DiagnosticResults(
            record=record_instance,
            results='Все хорошо, Вам осталось три дня :)'
        )
        diagnostic_result.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))