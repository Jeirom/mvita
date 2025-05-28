from django.test import TestCase
from mvita_main.models import Doctors, Reviews


class DoctorsModelTest(TestCase):
    def setUp(self):
        # Создаем объект Reviews для связи
        review = Reviews.objects.create(
            # добавьте необходимые поля, если есть
        )
        # Создаем тестового врача
        self.doctor = Doctors.objects.create(
            first_name="Иван",
            last_name="Иванов",
            specialization="Терапевт",
            experience="5 лет",
            reviews=review
        )

    def test_doctor_creation(self):
        doctor = Doctors.objects.get(id=self.doctor.id)
        self.assertEqual(doctor.first_name, "Иван")
        self.assertEqual(doctor.last_name, "Иванов")
        self.assertEqual(doctor.specialization, "Терапевт")
        self.assertEqual(doctor.experience, "5 лет")
        self.assertIsNotNone(doctor.reviews)
