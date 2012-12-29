from django.shortcuts import render
from market.models import Product
from events.models import Event
from polls.models import Poll


def home(request):
    infos = {}
    infos['products'] = Product.objects.all()[:3]
    infos['events'] = Event.objects.all()[:3]
    infos['polls'] = Poll.objects.all()[:3]
    return render(request, 'home.haml', infos)
