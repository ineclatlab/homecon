from django.contrib import admin
from fm.models import FmChange

class FmChangeAdmin(admin.ModelAdmin):
	list_display = ('fmchange_at','siliconid','packet')
	list_filter = ('fmchange_at',)
	search_fields = ('siliconid',)
admin.site.register(FmChange,FmChangeAdmin)

