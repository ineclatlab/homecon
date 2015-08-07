from django.db import models

class FmChange(models.Model):
	fmchange_at = models.DateTimeField(auto_now=True)
	packet  = models.TextField()
	siliconid = models.CharField(max_length=20)

	def __str__(self):
		return str(self.packet) 

