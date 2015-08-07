from django.db import models
import datetime
import pytz

def call_time_now():
	tz = pytz.timezone("Asia/Kolkata")
	time = (datetime.datetime.now(tz=tz))
	return time


class Pings(models.Model):
	ping_at = models.DateTimeField()
	packet  = models.TextField()
	siliconid = models.CharField(max_length=20)

	def __str__(self):
		return str(self.siliconid) 
