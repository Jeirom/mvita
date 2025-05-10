from requests import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from mvita_main.models import Doctors
from mvita_main.serializer import DoctorsSerializer


# from habit.paginators import HabitPagination
# from habit.permissions import IsOwnerOrPublic
# from habit.serializer import HabitSerializer


class DoctorsViewSet(ModelViewSet):

    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
