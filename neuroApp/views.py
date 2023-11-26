from django.shortcuts import render
from django.http import  HttpResponse
from django.views import  View
import logging

logger = logging.getLogger(__name__)
def neuro(request):
    logger.info('Получен доступ к странице нейросети')
    return HttpResponse("МЕТОД Работа нейросети будет здесь")

class NeuroWork(View):
    def get(self, request):
        logger.info('get Получен доступ к странице нейросети')
        return HttpResponse("КЛАСС Работа нейросети будет здесь")