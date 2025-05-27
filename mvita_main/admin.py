from .models import *

from django.contrib import admin








# # Направление в медицине
# @admin.register(Reviews)
# class ReviewsAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "description",)
#     list_filter = ("name",)
#     search_fields = ("name",)





# # Доктора
# @admin.register(Doctors)
# class DoctorsAdmin(admin.ModelAdmin):
#     list_display = ("id", "first_name", "last_name", "patronymic", "medical_direction",
#                     "avatar", "specialization", "experience", "user", )
#     list_filter = ("last_name", "specialization", "reviews", "medical_direction",)
#     search_fields = ("experience", "id", "medical_direction", )


# # Услуги
# @admin.register(Services)
# class ServicesAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "medical_direction", "description", "price", "user",)
#     list_filter = ("name", "description",)
#     search_fields = ("name", "description",)


# Информация
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ("id", 'info1', 'info2', 'info3', 'info4', 'info5', 'info6', 'info7', 'image_main', )
    # list_filter = ("address",)
    # search_fields = ("address",)

#
# # Ценности
# @admin.register(CompanyValues)
# class  CompanyValuesAdmin(admin.ModelAdmin):
#     list_display = ("name", "description", )
#
#
# # Запись на приём
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ("id", "status", "address", "doctor", "appointment_date", "services", "is_active", "user",)
#     list_filter = ("appointment_date", "user", "services")
#     search_fields = ("appointment_date", "user", "services")
#
#
# # Результаты диагностики
# @admin.register(DiagnosticResults)
# class DiagnosticResultsAdmin(admin.ModelAdmin):
#     list_display = ("id", "appointment", "recommendations", "user", "general_comments",)
#     list_filter = ("appointment",)
#     search_fields = ("appointment",)
#
#
# # Медицинские тесты. Результаты
# @admin.register(TestResult)
# class DiagnosticResultsAdmin(admin.ModelAdmin):
#     list_display = ("id", "diagnostic_result", "name", "value", "norm", "comment",)
#     list_filter = ("name",)
#     search_fields = ("name",)
#
#
# # Обратная связь
# @admin.register(Feedback)
# class  CompanyValuesAdmin(admin.ModelAdmin):
#     list_display = ("subject", "feedback", "user", "created_at",)