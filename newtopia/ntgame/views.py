from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models.province import Province
from .forms import BuildOrderForm

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
    this_page = 'throne'
    context = {
        'province': province,
        'game': game,
        'this_page': this_page,
    }
    return HttpResponse(template.render(context, request))


@login_required()
def build(request):
    province = Province.objects.get(pk=request.user.id)
    template = loader.get_template('ntgame/building.html')
    this_page = 'build'

    context = {
        'province': province,
        'this_page': this_page,
    }

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BuildOrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # template = building-summary.html
            return HttpResponse(template.render(context, request))
    else:
        form = BuildOrderForm()

    context['form'] = form
    return HttpResponse(template.render(context, request))
