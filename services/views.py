from django.shortcuts import render, HttpResponse
from .models import Pings
from fm.models import FmChange
import datetime
import pytz


def pingpacket(request):
	sPingPacket = request.GET.get('pkt', '')
	tz = pytz.timezone("Asia/Kolkata")
	time = (datetime.datetime.now(tz=tz))
	sSiliconid = sPingPacket[1:17]
	p = Pings(packet=sPingPacket, siliconid=sSiliconid,ping_at=time)
	p.save()
	s = FmChange.objects.latest('id')
	s = str(s)
	s = s[2:-2]
	return HttpResponse(s)