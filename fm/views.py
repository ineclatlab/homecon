from django.shortcuts import render, HttpResponse
import datetime
import pytz
from .models import FmChange

def fmchange(request):
	if request.method == 'POST':
		sFMValue = request.POST.getlist('sFM')
		tz = pytz.timezone("Asia/Kolkata")
		time = (datetime.datetime.now(tz=tz))
		sSiliconid = "181E0BC8000E1440"
		p = FmChange(packet=sFMValue, siliconid=sSiliconid,fmchange_at=time)
		p.save()
	return render(request,"fm/fm.html")


def save_fm_settings(request):
	print ("jhkjdshkjs")
	if request.method == 'POST':
		print ("OK sucess")
	return render(request,"fm/fm.html")