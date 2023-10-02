from django.shortcuts import render
from firstApp.models import AccessRecord ,Topic, Webpage

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    context = {'access_records': webpages_list}
    return render(request, 'firstApp/index.html', context)
