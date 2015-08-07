from django.contrib import admin
from services.models import Pings

class PingsAdmin(admin.ModelAdmin):
	list_display = ('ping_at','siliconid','packet')
	list_filter = ('ping_at',)
	search_fields = ('siliconid',)
admin.site.register(Pings,PingsAdmin)

