from django.shortcuts import render
from django.http import JsonResponse
from  .models import Country
from  .models import Language
from  .models import Channels

# Create your views here.
def home_action(request):
    country_id = int(request.POST.get('country_id','0'))
    language_id = int(request.POST.get('language_id','0'))

    country_result = Country.objects.all()
    if not country_id :
        country_id = 1

    language_result = Language.objects.filter(country_id=country_id)
    if not language_id :
        language_id = 2

    channels_list_result = Channels.objects.filter(country_id=country_id, language_id=language_id)

    return render(request, 'applive/home.html', locals())


def settings(request) :
    prev_country_id = 0
    prev_language_id = 0
    country_list = Country.objects.all()
    language_list = Language.objects.all()

    return render(request, 'applive/settings.html', locals())
