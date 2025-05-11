from rest_framework.serializers import ModelSerializer

from mvita_main.models import (
    Doctors,
    Record,
    Reviews,
    Information,
    DiagnosticResults,
    Services,
)


class DoctorsSerializer(ModelSerializer):
    """Сериалайзер для Doctors. Включает все поля"""

    class Meta:
        model = Doctors
        fields = "__all__"


class RecordSerializer(ModelSerializer):
    """Сериалайзер для Record. Включает все поля"""

    class Meta:
        model = Record
        fields = "__all__"


class ReviewsSerializer(ModelSerializer):
    """Сериалайзер для Reviews. Включает все поля"""

    class Meta:
        model = Reviews
        fields = "__all__"


class InformationSerializer(ModelSerializer):
    """Сериалайзер для Information. Включает все поля"""

    class Meta:
        model = Information
        fields = "__all__"


class ServicesSerializer(ModelSerializer):
    """Сериалайзер для Services. Включает все поля"""

    class Meta:
        model = Services
        fields = "__all__"


class DiagnosticResultsSerializer(ModelSerializer):
    """Сериалайзер для DiagnosticResults. Включает все поля"""

    class Meta:
        model = DiagnosticResults
        fields = "__all__"
