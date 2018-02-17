from django.http import HttpResponse
from django.views import generic
from .models import Threat

class IndexView(generic.ListView):
    template_name = 'threatapp/index.html'
    context_object_name = 'threats_list'
    paginate_by = 20
    
    def get_queryset(self):
        return Threat.objects.order_by('date')

def uploadfile(request):
    return HttpResponse("TODO: change this to upload json file")