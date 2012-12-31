from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from crowdsourcing.models import Survey
from django.conf import settings
from market.models import Product
from events.models import Event
from forms import ContactForm


@login_required
def home(request):
    infos = {}
    infos['products'] = Product.objects.all()[:3]
    infos['events'] = Event.objects.all()[:1]
    return render(request, 'home.haml', infos)


@login_required
def survey(request):
    survey = None
    surveys = Survey.live.order_by('-survey_date')
    if surveys:
        survey = surveys[0]
    return render(request, 'survey.haml', {'survey': survey})


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data['message'] + "\n\n\n" + ('-' * 80)
            msg += "\n\n Ip : " + request.META["REMOTE_ADDR"]
            send_mail(form.cleaned_data['subject'],
                      msg,
                      request.user.email,
                      [row[1] for row in settings.ADMINS],
                      fail_silently=True)
            return render(request, 'contact_ok.haml', {'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, "contact.haml", {'form': form})
