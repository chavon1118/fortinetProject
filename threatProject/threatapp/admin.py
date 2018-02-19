from django.contrib import admin

from .models import Threat, MetaFile

class ThreatAdmin(admin.ModelAdmin):
    list_display = ('filename','action','submit_type','rating','date')

admin.site.register(Threat, ThreatAdmin)
admin.site.register(MetaFile)