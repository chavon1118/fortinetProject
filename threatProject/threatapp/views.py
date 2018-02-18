import json
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.urls import reverse
from .models import Threat

class IndexView(generic.ListView):
    template_name = 'threatapp/index.html'
    context_object_name = 'threats_list'
    paginate_by = 20
    
    def get_queryset(self):
        return Threat.objects.order_by('date')

def uploadfile(request):
    if request.method == 'POST':
        threatfile = request.FILES['threatfile']
        for chunk in threatfile.chunks():
            print("chunk: %s" %chunk)
            data = json.loads(chunk.decode('utf-8').replace("'",'"'))
            print("data: %s" %data)
            for threat in data:
                Threat.objects.update_or_create(date=datetime.strptime(threat['date'],'%b %d, %Y %H:%M:%S'), filename=threat['filename'],
                action=threat['action'],submit_type=threat['submit-type'],rating=threat['rating'])
    return HttpResponseRedirect(reverse('threatapp:index'))