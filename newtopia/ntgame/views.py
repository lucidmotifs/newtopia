from django.shortcuts import render

from .models import Province

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


def throne(request, province_id):
    province = Province.objects.get(pk=province_id)
    template = loader.get_template('ntgame/throne.html')
    context = {
        'province': province,
    }
    return HttpResponse(template.render(context, request))
