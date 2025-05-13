from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("mvita/", include("mvita_main.urls", namespace="mvita")),
    path("users/", include("users.urls", namespace="users")),
]
