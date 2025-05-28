from mvita_main.models import Doctors, Information, DiagnosticResults, Record, Services

from django.contrib import admin




# Информация
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "info1",
        "info2",
        "info3",
        "info4",
        "info5",
        "info6",
        "info7",
        "image_main",
    )


# Доктор
@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "experience",
        "image",
        "specialization",
    )

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'appointment_date', 'address')
    search_fields = ('patient_name',)
    list_filter = ('address', 'doctor')

@admin.register(DiagnosticResults)
class DiagnosticResultsAdmin(admin.ModelAdmin):
    list_display = ('user', 'record', 'results')
    search_fields = ('results',)
    list_filter = ('user',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('name',)