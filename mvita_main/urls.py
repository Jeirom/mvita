from rest_framework.routers import SimpleRouter
from django.urls import path, include
from mvita_main.apps import MvitaMainConfig
from mvita_main.views import DoctorsViewSet


app_name = MvitaMainConfig.name

router = SimpleRouter()
router.register("doctors", DoctorsViewSet)

urlpatterns = [
]



urlpatterns += router.urls
