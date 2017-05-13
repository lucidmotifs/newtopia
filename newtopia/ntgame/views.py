from django.shortcuts import render

from .models.province import Province

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# Auhorization stuff
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


@login_required()
def throne(request):
    class Game:
        day = 1
        month = "Jan"
        year = 1

    province = Province.objects.get(pk=request.user.id)
    game = Game()
    template = loader.get_template('ntgame/throne.html')
    context = {
        'province': province,
        'game': game
    }
    return HttpResponse(template.render(context, request))
