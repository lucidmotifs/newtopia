from django.shortcuts import render

from .models import Province

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# Auhorization stuff
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


def throne(request, province_id):
    class Game:
        day = 1
        month = "Jan"
        year = 1


    province = Province.objects.get(pk=province_id)
    game = Game()
    template = loader.get_template('ntgame/throne.html')
    context = {
        'province': province,
        'game': game
    }
    return HttpResponse(template.render(context, request))
