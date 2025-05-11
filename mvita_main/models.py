from django.db import models
from django.db.models import CASCADE


class Reviews(models.Model):
    """
    Модель для хранения отзывов о врачах.

    Attributes:
        DOCTOR_RATE (list[tuple[str, str]]): Список возможных оценок и их описаний.
        text (str): Текст отзыва, может быть пустым.
        rate (str): Оценка врача в виде звезд, выбирается из DOCTOR_RATE.
    """

    DOCTOR_RATE: list[tuple[str, str]] = [
        ("5", "Все отлично!"),
        ("4", "Все хорошо."),
        ("3", "Есть замечания"),
        ("2", "Не устроило"),
        ("1", "Категорически не устроило"),
    ]

    text = models.CharField(max_length=255, verbose_name="Отзыв", blank=True, null=True)
    rate = models.CharField(
        verbose_name="Количество звезд", max_length=10, choices=DOCTOR_RATE
    )


class Doctors(models.Model):
    """
    Модель для хранения информации о врачах.

    Attributes:
        first_name (str): Имя врача.
        last_name (str): Фамилия врача.
        specialization (str): Специальность врача.
        experience (str): Стаж работы врача.
        reviews (ForeignKey): Связь с моделью Reviews для хранения отзывов.
    """

    first_name = models.CharField(
        max_length=255, verbose_name="Имя", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255, verbose_name="Фамилия", null=True, blank=True
    )
    specialization = models.CharField(
        max_length=255, verbose_name="Специальность", null=True, blank=True
    )
    experience = models.CharField(
        max_length=255, verbose_name="Стаж работы", null=True, blank=True
    )
    reviews = models.ForeignKey(
        Reviews,
        verbose_name="Отзывы на врача",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )


class Services(models.Model):
    """
    Модель для хранения информации о медицинских услугах.
    """

    name = models.CharField(
        max_length=255, verbose_name="Название услуги", blank=True, null=True
    )
    description = models.CharField(
        max_length=255, verbose_name="Описание услуги", blank=True, null=True
    )


class Information(models.Model):
    """
    Модель для хранения контактной информации клиники.

    Attributes:
        phone (str): Номер телефона клиники.
        address (str): Адрес клиники.
    """

    phone = models.CharField(
        max_length=255, verbose_name="Номер телефона", null=True, blank=True
    )
    address = models.CharField(
        max_length=255, verbose_name="Адрес клиники", null=True, blank=True
    )
    information = models.CharField(
        max_length=255, verbose_name="Главная информация", blank=True, null=True
    )


class Record(models.Model):
    """
    Модель для хранения записей пациентов на прием к врачам.

    Attributes:
        ADDRES_CLINIC (list[tuple[str, str]]): Список адресов клиник, доступных для записи.
        addres (str): Адрес клиники, выбирается из ADDRES_CLINIC.
        doctor (ForeignKey): Связь с моделью Doctors, указывающая на врача, к которому записан пациент.
        patient_name (str): Имя пациента.
        appointment_date (datetime): Дата и время записи на прием.
        services (ForeignKey): Связь с моделью Services, указывающая на услуги, которые будут предоставлены.
    """

    ADDRES_CLINIC = [
        ("Клиника на Малыгина", "Ул.Малыгина 44, 1 этаж"),
        ("Клиника на Федюнинского", "Ул.Федюнинского 3, 1 этаж"),
    ]
    addres = models.CharField(
        max_length=255,
        verbose_name="Адрес клиники",
        null=True,
        blank=True,
        choices=ADDRES_CLINIC,
    )
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    services = models.ForeignKey(Services, on_delete=CASCADE)


class DiagnosticResults(models.Model):
    """
    Модель для хранения результатов диагностики, связанных с записями пациентов.

    Attributes:
        record (ForeignKey): Связь с моделью Record, указывающая на запись, к которой относятся результаты.
        results (str): Результаты диагностики, могут быть пустыми.
    """

    record = models.ForeignKey(
        Record,
        max_length=255,
        verbose_name="Запись",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    results = models.CharField(
        max_length=255, verbose_name="Результаты диагностики", null=True, blank=True
    )
