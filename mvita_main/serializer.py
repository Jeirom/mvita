from rest_framework.serializers import ModelSerializer

from mvita_main.models import Doctors


class DoctorsSerializer(ModelSerializer):
    """Сериалайзер для Habit. Включает все поля"""

    class Meta:
        model = Doctors
        fields = "__all__"
