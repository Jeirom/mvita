from django.core.management import BaseCommand

from mvita_main.models import Services


class Command(BaseCommand):
    help = "Добавляет данные в таблицу Services"

    def handle(self, *args, **kwargs):
        # Диагностические услуги
        services = [
            {
                "name": "МРТ головного мозга",
                "description": "Высокоточная магнитно-резонансная томография для выявления патологий мозга.",
                "price": "3000",
            },
            {
                "name": "УЗИ брюшной полости",
                "description": "Обследование внутренних органов брюшной полости с помощью ультразвука.",
                "price": "1500",
            },
            {
                "name": "ЭКГ (электрокардиограмма)",
                "description": "Диагностика работы сердца с помощью электрокардиографа.",
                "price": "800",
            },
            {
                "name": "Колоноскопия",
                "description": "Исследование кишечника с помощью гибкой трубки для выявления патологий.",
                "price": "4500",
            },
            {
                "name": "Анализ крови на сахар",
                "description": "Определение уровня глюкозы в крови для диагностики диабета.",
                "price": "400",
            },
            {
                "name": "Рентгенография легких",
                "description": "Обследование легких для выявления воспалений, опухолей и других патологий.",
                "price": "1200",
            },
            {
                "name": "Дуплексное сканирование сосудов",
                "description": "Оценка кровотока и состояния сосудов с помощью ультразвука.",
                "price": "2500",
            },
        ]

        for service in services:
            my_instance = Services(
                name=service["name"],
                description=service["description"],
                price=service["price"],
            )
            my_instance.save()

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
