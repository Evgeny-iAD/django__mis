from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
import logging

from django.views.generic import TemplateView
from .models import Pacient
from django.db.models import Q

logger = logging.getLogger(__name__)

def mis(request):
    logger.info('Получен доступ к странице картотеки МИС')
    return HttpResponse("МЕТОД Картотека из МИС будет здесь")


def get_patient_info(request, patient_id):
    patient = Pacient.objects.get(id=patient_id)
    return JsonResponse({
        'full_name': f"{patient.last_name} {patient.first_name} {patient.patronymic}",
        'birth_date': f"{patient.birth_date}",
        'gender': f"{patient.sex}",
        'code': f"{patient.code}",
        'snils': f"{patient.snils}",
        'attachment': f"{patient.attachment}",
        'document': f"{patient.document}",
        'polis': f"{patient.polis}",
        'address': f"{patient.address}",
        'fluorography': f"{patient.fluorography}",
    })
class MisWork(TemplateView):
    template_name = "misApp/mis_kartoteka.html"
    def get_context_data(self, **kwargs):
        logger.info('Контекст get_context_data')
        context = super().get_context_data(**kwargs)
        # Получение данных о всех пациентах из базы данных
        patients = Pacient.objects.all()
        # Добавление списка пациентов в контекст
        context['patients'] = patients
        return context

    def post(self, request, *args, **kwargs):
        # Сохранение фильтра в сессии
        request.session['filter'] = request.POST
        # Получение данных из формы
        codname = request.POST.get('codname')
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        snils = request.POST.get('snils')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        # Добавьте другие поля, если они есть

        # Использование Q-объектов для сложных запросов
        q_objects = Q()  # Создаем пустой Q-объект

        # Добавляем условия фильтрации, если поля заполнены
        if codname:
            q_objects &= Q(code=codname)
        if surname:
            q_objects &= Q(last_name__icontains=surname)
        if name:
            q_objects &= Q(first_name__icontains=name)
        if patronymic:
            q_objects &= Q(patronymic__icontains=patronymic)
        if snils:
            q_objects &= Q(snils__icontains=snils)
        if date_from:
            q_objects &= Q(birth_date__gte=date_from)
        if date_to:
            q_objects &= Q(birth_date__lte=date_to)
        # Добавьте другие условия, если они есть

        # Фильтрация пациентов по критериям
        patients = Pacient.objects.filter(q_objects)


        # Передача отфильтрованных пациентов в контекст и отрисовка шаблона
        context = {'patients': patients,
                   'filter': self.request.session.get('filter', {})}
        # Загрузка фильтра из сессии
        # context['filter'] = self.request.session.get('filter', {})
        return render(request, self.template_name, context)

