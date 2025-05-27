from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


#################### Doctors Views ####################


class DoctorsListView(ListView):
    """
    Отображает список всех врачей.
    Используется для просмотра и выбора врача из базы данных.
    """

    model = Doctors
    fields = ["first_name", "last_name", "specialization"]
    template_name = "../templates/doctors/doctors_form.html"
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        """
        Добавляет дополнительные данные в контекст, такие как список всех врачей и информация.
        """
        context = super().get_context_data(**kwargs)
        context["doctors"] = Doctors.objects.all()
        context["info"] = get_object_or_404(Information, id=3)
        # context['image'] = get_object_or_404(Information, id=5)
        return context


class DoctorsCreateView(CreateView):
    """
    Обеспечивает создание нового врача.
    После успешного добавления перенаправляет на страницу формы врачей.
    """

    model = Doctors
    template_name = "../templates/doctors/doctors_create.html"
    fields = ["first_name", "last_name", "specialization"]
    success_url = reverse_lazy("mvita:doctors_form")


class DoctorsDetailView(DetailView):
    """
    Отображает подробную информацию о выбранном враче.
    """

    model = Doctors
    fields = ["first_name", "last_name", "specialization"]
    template_name = "../templates/doctors/doctors_detail.html"
    context_object_name = "doctors"


class DoctorsUpdateView(UpdateView):
    """
    Позволяет редактировать информацию о враче.
    """

    model = Doctors
    template_name = "../templates/doctors/doctors_update.html"
    fields = ["first_name", "last_name", "specialization"]


class DoctorsDeleteView(DeleteView):
    """
    Обеспечивает удаление врача из базы данных.
    После удаления перенаправляет на список врачей.
    """

    model = Doctors
    template_name = "../templates/doctors/doctors_delete.html"
    success_url = reverse_lazy("mvita:doctors_form")


#################### Reviews Views ####################


class ReviewsListView(ListView):
    """
    Отображает список всех отзывов.
    """

    model = Reviews
    # fields = ['first_name', 'last_name', 'specialization']
    template_name = "../templates/reviews/reviews_form.html"
    context_object_name = "reviews"


class ReviewsCreateView(CreateView):
    """
    Создает новый отзыв.
    После успешного добавления возвращает на страницу отзывов.
    """

    model = Reviews
    template_name = "reviews_create.html"
    # fields = ['first_name', 'last_name', 'specialization']
    success_url = reverse_lazy("mvita:doctors_form")


class ReviewsDetailView(DetailView):
    """
    Показывает подробную информацию о конкретном отзыве.
    """

    model = Reviews
    template_name = "reviews_detail.html"
    context_object_name = "reviews"


class ReviewsUpdateView(UpdateView):
    """
    Позволяет редактировать существующий отзыв.
    """

    model = Reviews
    template_name = "reviews_update.html"
    # fields = ['first_name', 'last_name', 'specialization']


class ReviewsDeleteView(DeleteView):
    """
    Удаляет отзыв из базы данных.
    После удаления возвращает на страницу отзывов.
    """

    model = Reviews
    template_name = "reviews_delete.html"
    success_url = reverse_lazy("mvita:reviews_form")


#################### Services Views ####################


class ServicesDeleteView(DeleteView):
    """
    Удаляет услугу из базы данных.
    """

    model = Services
    template_name = "../templates/services/delete_form.html"
    success_url = reverse_lazy("mvita:services_form")


class ServicesListView(ListView):
    """
    Отображает список всех услуг.
    """

    model = Services
    context_object_name = "services"
    template_name = "../templates/services/services_form.html"


class ServicesCreateView(CreateView):
    """
    Создает новую услугу.
    """

    model = Services
    template_name = "services_create.html"
    success_url = reverse_lazy("mvita:services_form")


class ServicesUpdateView(UpdateView):
    """
    Позволяет редактировать существующую услугу.
    """

    model = Services
    template_name = "services_update.html"


class ServicesDetailView(DetailView):
    """
    Показывает подробную информацию о выбранной услуге.
    """

    model = Services
    template_name = "services_detail.html"
    context_object_name = "services"


#################### Information Views ####################


class InformationListView(ListView):
    """
    Отображает список информации о компании.
    """

    model = Information
    template_name = "../templates/information/information_form.html"
    success_url = reverse_lazy("mvita:information_form")
    context_object_name = "info"


class InformationCreateView(CreateView):
    """
    Создает новую запись информации.
    """

    model = Information
    template_name = "information_create.html"
    success_url = reverse_lazy("mvita:information_form")


class InformationUpdateView(UpdateView):
    """
    Позволяет редактировать существующую информацию.
    """

    model = Information
    template_name = "information_update.html"


class InformationDetailView(DetailView):
    """
    Показывает подробную информацию о выбранной записи.
    """

    model = Information
    template_name = "information_detail.html"
    context_object_name = "info"


class InformationDeleteView(DeleteView):
    """
    Удаляет запись информации.
    """

    model = Information
    template_name = "information_delete.html"
    success_url = reverse_lazy("mvita:information_form")


#################### Record Views ####################


class RecordListView(ListView):
    """
    Отображает список записей на прием текущего пользователя.
    """

    model = Record
    template_name = "../templates/record/record_form.html"
    context_object_name = "record"

    def get_queryset(self):
        """
        Фильтрует записи по текущему пользователю.
        """
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class RecordCreateView(CreateView):
    """
    Создает новую запись на прием.
    """

    model = Record
    form_class = RecordForm
    template_name = "../templates/record/record_create.html"
    success_url = reverse_lazy("mvita:record")

    def get_context_data(self, **kwargs):
        """
        Передает в контекст список врачей, услуг и адреса клиники.
        """
        context = super().get_context_data(**kwargs)
        context["doctors"] = Doctors.objects.all()
        context["services"] = Services.objects.all()
        context["ADDRES_CLINIC"] = [
            ("ул. Ленина, д.1", "Клиника на Малыгина"),
        ]
        return context

    def form_valid(self, form):
        """
        Присваивает текущего пользователя новой записи.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    """
    Позволяет редактировать существующую запись.
    """

    model = Record
    template_name = "record_update.html"


class RecordDetailView(DetailView):
    """
    Отображает подробную информацию о записи.
    """

    model = Record
    template_name = "record_detail.html"
    context_object_name = "record"


class RecordDeleteView(DeleteView):
    """
    Удаляет запись на прием.
    """

    model = Record
    template_name = "record_delete.html"
    success_url = reverse_lazy("mvita:record")


#################### DiagnosticResults Views ####################


class DiagnosticListView(ListView):
    """
    Отображает список результатов диагностики текущего пользователя.
    """

    model = DiagnosticResults
    template_name = "../templates/diagnostic/diagnostic_form.html"
    context_object_name = "diagnostic"

    def form_valid(self, form):
        """
        Присваивает текущего пользователя результату диагностики.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class DiagnosticCreateView(CreateView):
    """
    Создает новый результат диагностики.
    """

    model = DiagnosticResults
    template_name = "diagnostic_create.html"
    success_url = reverse_lazy("mvita:diagnostic_form")


class DiagnosticUpdateView(UpdateView):
    """
    Позволяет редактировать результат диагностики.
    """

    model = DiagnosticResults
    template_name = "diagnostic_update.html"


class DiagnosticDetailView(DetailView):
    """
    Показывает подробную информацию о результате диагностики.
    """

    model = DiagnosticResults
    template_name = "diagnostic_detail.html"
    context_object_name = "record"


class DiagnosticDeleteView(DeleteView):
    """
    Удаляет результат диагностики.
    """

    model = DiagnosticResults
    template_name = "diagnostic_delete.html"
    success_url = reverse_lazy("mvita:diagnostic_form")


#################### Other's Views ####################


def history_view(request) -> HttpResponse:
    """
    Отображает страницу истории компании.
    """
    info = Information.objects.get(name="основная")
    context = {
        "name": info.name,
        "info1": info.info1,
        "info2": info.info2,
        "info3": info.info3,
        "info4": info.info4,
        "info5": info.info5,
        "info6": info.info6,
        "info7": info.info7,
    }
    return render(request, "../templates/other/history.html", context=context)
