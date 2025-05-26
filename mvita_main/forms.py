from django import forms
from .models import Services, Doctors, Record


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = "__all__"


class RecordForm(forms.ModelForm):
    address = forms.ChoiceField(
        choices=[
            ("ул. Малыгина 44", "Клиника на Малыгина"),
        ],
        label="Адрес клиники",
        widget=forms.Select(attrs={"class": "form-control", "required": True}),
    )
    patient_name = forms.CharField(
        max_length=100,
        label="Имя пациента",
        widget=forms.TextInput(
            attrs={"class": "form-control", "maxlength": "100", "required": True}
        ),
    )
    appointment_date = forms.DateTimeField(
        label="Дата и время",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control", "required": True}
        ),
    )
    services = forms.ModelChoiceField(
        queryset=Services.objects.all(),
        label="Услуга",
        widget=forms.Select(attrs={"class": "form-control", "required": True}),
    )
    # doctors_id = forms.ModelChoiceField(
    #     queryset=Doctors.objects.all(),
    #     label='Доктор',
    #     widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    # )

    class Meta:
        model = Record
        fields = ["address", "patient_name", "appointment_date", "services"]
