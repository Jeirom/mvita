from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)

from mvita_main.forms import RecordForm
from mvita_main.models import (
    Doctors,
    Record,
    Reviews,
    Information,
    DiagnosticResults,
    Services,
)


#################### Doctors Views  ####################


class DoctorsListView(ListView):
    model = Doctors
    fields = ["first_name", "last_name", "specialization"]
    template_name = "../templates/doctors/doctors_form.html"
    context_object_name = "doctors"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctors.objects.all()
        context['info'] = get_object_or_404(Information, id=4)
        return context


class DoctorsCreateView(CreateView):
    model = Doctors
    template_name = "../templates/doctors/doctors_create.html"
    fields = ["first_name", "last_name", "specialization"]
    success_url = reverse_lazy("mvita:doctors_form")


class DoctorsDetailView(DetailView):
    model = Doctors
    fields = ["first_name", "last_name", "specialization"]
    template_name = "../templates/doctors/doctors_detail.html"
    context_object_name = "doctors"


class DoctorsUpdateView(UpdateView):
    model = Doctors
    template_name = "../templates/doctors/doctors_update.html"
    fields = ["first_name", "last_name", "specialization"]


class DoctorsDeleteView(DeleteView):
    model = Doctors
    template_name = "../templates/doctors/doctors_delete.html"
    success_url = reverse_lazy("mvita:doctors_form")


#################### Reviews Views  ####################


class ReviewsListView(ListView):
    model = Reviews
    # fields = ['first_name', 'last_name', 'specialization']
    template_name = "../templates/reviews/reviews_form.html"
    context_object_name = "reviews"


class ReviewsCreateView(CreateView):
    model = Reviews
    template_name = "reviews_create.html"
    # fields = ['first_name', 'last_name', 'specialization']
    success_url = reverse_lazy("mvita:doctors_form")


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = "reviews_detail.html"
    context_object_name = "reviews"


class ReviewsUpdateView(UpdateView):
    model = Reviews
    template_name = "reviews_update.html"
    # fields = ['first_name', 'last_name', 'specialization']


class ReviewsDeleteView(DeleteView):
    model = Reviews
    template_name = "reviews_delete.html"
    success_url = reverse_lazy("mvita:reviews_form")


#################### Services Views  ####################


class ServicesDeleteView(DeleteView):
    model = Services
    template_name = "../templates/services/delete_form.html"
    success_url = reverse_lazy("mvita:services_form")


class ServicesListView(ListView):
    model = Services
    context_object_name = "services"
    template_name = "../templates/services/services_form.html"

class ServicesCreateView(CreateView):
    model = Services
    template_name = "services_create.html"
    success_url = reverse_lazy("mvita:services_form")


class ServicesUpdateView(UpdateView):
    model = Services
    template_name = "services_update.html"


class ServicesDetailView(DetailView):
    model = Services
    template_name = "services_detail.html"
    context_object_name = "services"


#################### Information Views  ####################


class InformationListView(ListView):
    model = Information
    template_name = "../templates/information/information_form.html"
    success_url = reverse_lazy("mvita:information_form")
    context_object_name = "info"


class InformationCreateView(CreateView):
    model = Information
    template_name = "information_create.html"
    success_url = reverse_lazy("mvita:information_form")


class InformationUpdateView(UpdateView):
    model = Information
    template_name = "information_update.html"


class InformationDetailView(DetailView):
    model = Information
    template_name = "information_detail.html"
    context_object_name = "info"


class InformationDeleteView(DeleteView):
    model = Information
    template_name = "information_delete.html"
    success_url = reverse_lazy("mvita:information_form")


#################### Record Views  ####################


class RecordListView(ListView):
    model = Record
    template_name = "../templates/record/record_form.html"
    context_object_name = "record"


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = "../templates/record/record_create.html"
    success_url = reverse_lazy("mvita:record")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctors.objects.all()
        context['services'] = Services.objects.all()
        context['ADDRES_CLINIC'] = [
            ('ул. Ленина, д.1', 'Клиника на Малыгина'),
        ]
        return context

    def form_valid(self, form):
        print("Форма валидна")
        print("POST данные:", self.request.POST)
        # В форме уже есть все необходимые поля, их можно оставить
        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    model = Record
    template_name = "record_update.html"


class RecordDetailView(DetailView):
    model = Record
    template_name = "record_detail.html"
    context_object_name = "record"


class RecordDeleteView(DeleteView):
    model = Record
    template_name = "record_delete.html"
    success_url = reverse_lazy("mvita:record_form")


#################### DiagnosticResults Views  ####################


class DiagnosticListView(ListView):
    model = DiagnosticResults
    template_name = "../templates/diagnostic/diagnostic_form.html"
    context_object_name = "diagnostic"


class DiagnosticCreateView(CreateView):
    model = DiagnosticResults
    template_name = "diagnostic_create.html"
    success_url = reverse_lazy("mvita:diagnostic_form")


class DiagnosticUpdateView(UpdateView):
    model = DiagnosticResults
    template_name = "diagnostic_update.html"


class DiagnosticDetailView(DetailView):
    model = DiagnosticResults
    template_name = "diagnostic_detail.html"
    context_object_name = "record"


class DiagnosticDeleteView(DeleteView):
    model = DiagnosticResults
    template_name = "diagnostic_delete.html"
    success_url = reverse_lazy("mvita:diagnostic_form")


#################### Other's Views  ####################


def history_view(request) -> HttpResponse:
    """
    Контроллер для отображения истории компании.

    :param request: HTTP запрос
    :return: HttpResponse
    """
    info = Information.objects.get(name='основная')
    context = {
        'name': info.name,
        'info1': info.info1,
        'info2': info.info2,
        'info3': info.info3,
        'info4': info.info4,
        'info5': info.info5,
        'info6': info.info6,
        'info7': info.info7,
    }
    return render(request, "../templates/other/history.html", context=context)