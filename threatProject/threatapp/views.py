import json
import os
from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.shortcuts import render
from django.urls import reverse
from .models import Threat, MetaFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# for displaying table of threats, default order by date
class IndexView(generic.ListView):
    template_name = 'threatapp/index.html'
    context_object_name = 'threats_list'
    paginate_by = 20
    
    def get_queryset(self):
        return Threat.objects.order_by('date')

# user can upload json meta file to add threats to database
def uploadfile(request):
    if request.method == 'POST' and request.FILES['threatfile']:
        threatfile = request.FILES['threatfile']
        # save file to media dir
        fs = FileSystemStorage()
        filename = fs.save(threatfile.name, threatfile)
        uploaded_file_url = fs.url(filename)
        data = updateDatabase(threatfile)
        MetaFile.objects.create(filename=filename,is_imported=False)
        response = {'uploaded_file_url': uploaded_file_url, 'data': data}
        return JsonResponse(response)
    return HttpResponseRedirect(reverse('threatapp:index'))

# check for unprocessed meta file in folder and
# notify dom to update
def checkupdate(request):
    if request.method == 'GET':
        #filenames = MetaFile.objects.filter(is_imported=False).values_list('filename', flat=True)
        fs = FileSystemStorage(settings.MEDIA_ROOT)
        data = []
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for file in files:
                if file.endswith(".json"):
                    file_record = MetaFile.objects.filter(filename=file).count()
                    if file_record == 0:
                        threatfile = fs.open(file)
                        data.append(updateDatabase(threatfile))
                        MetaFile.objects.create(filename=file,is_imported=True)
                        print(os.path.join(settings.MEDIA_ROOT, file))
        return JsonResponse({"data": data})

def updateDatabase(threatfile):
    for chunk in threatfile.chunks():
        data = json.loads(chunk.decode('utf-8').replace("'",'"'))
        for threat in data:
            Threat.objects.update_or_create(date=datetime.strptime(threat['date'],'%b %d, %Y %H:%M:%S'), filename=threat['filename'],
            action=threat['action'],submit_type=threat['submit-type'],rating=threat['rating'])
    return data