from django.conf.urls import include, url

urlpatterns = [
	url(r'','fm.views.fmchange'),
	url(r'^save_fm_settings','fm.views.save_fm_settings',name='save_fm_settings'),
]