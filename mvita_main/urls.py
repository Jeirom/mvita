from rest_framework.routers import SimpleRouter
from django.urls import path, include
from mvita_main.apps import MvitaMainConfig
from mvita_main.views import (
    DoctorsListView,
    DoctorsCreateView,
    DoctorsDeleteView,
    DoctorsDetailView,
    DoctorsUpdateView,
)


app_name = "mvita"

urlpatterns = [
    path("", DoctorsListView.as_view()),
    path("<int:pk>/", DoctorsDetailView.as_view(), name="myblog_detail"),
    path("new/", DoctorsCreateView.as_view(), name="myblog_create"),
    path("<int:pk>/edit/", DoctorsUpdateView.as_view(), name="myblog_edit"),
    path("<int:pk>/delete/", DoctorsDeleteView.as_view(), name="myblog_delete"),
]
