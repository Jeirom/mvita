from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mvita_main.models import (
    Doctors,
    Record,
    Reviews,
    Information,
    DiagnosticResults,
    Services,
)
from mvita_main.serializer import (
    DoctorsSerializer,
    RecordSerializer,
    ReviewsSerializer,
    InformationSerializer,
    ServicesSerializer,
    DiagnosticResultsSerializer,
)


class DoctorsViewSet(ModelViewSet):
    """
    ViewSet для управления записями врачей.

    Этот ViewSet предоставляет стандартные действия для работы с моделями Doctors,
    включая получение списка врачей, создание нового врача, обновление и удаление.
    """
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer


class RecordViewSet(ModelViewSet):
    """
    ViewSet для управления записями пациентов.

    Этот ViewSet предоставляет стандартные действия для работы с моделями Record,
    включая получение списка записей, создание новой записи, обновление и удаление.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class ReviewsViewSet(ModelViewSet):
    """
    ViewSet для управления отзывами.

    Этот ViewSet предоставляет стандартные действия для работы с моделями Reviews,
    включая получение списка отзывов, создание нового отзыва, обновление и удаление.
    """
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class DiagnosticResultsViewSet(ModelViewSet):
    """
    ViewSet для управления диагностическими результатами.

    Этот ViewSet предоставляет стандартные действия для работы с моделями DiagnosticResults,
    включая получение списка результатов, создание нового результата, обновление и удаление.
    """
    queryset = DiagnosticResults.objects.all()
    serializer_class = DiagnosticResultsSerializer


class ServicesViewSet(ModelViewSet):
    """
    ViewSet для управления услугами.

    Этот ViewSet предоставляет стандартные действия для работы с моделями Services,
    включая получение списка услуг, создание новой услуги, обновление и удаление.
    """
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class InformationViewSet(ModelViewSet):
    """
    ViewSet для управления информацией.

    Этот ViewSet предоставляет стандартные действия для работы с моделями Information,
    включая получение списка информации, создание новой информации, обновление и удаление.
    """
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
