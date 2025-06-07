from django.contrib import admin
from users.models import User


@admin.register(User)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "avatar",
        "phone",
        "city",
        "token",
        "is_active",
        "country",
    )