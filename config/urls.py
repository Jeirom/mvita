from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("doctors/", include("mvita_main.urls", namespace="doctors")),
]
