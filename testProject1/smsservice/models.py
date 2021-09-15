from django.db import models
from formpage1.models import SessionModel, Justifications
import uuid


class SmsCodeModel(models.Model):
	smscode_id = models.IntegerField(primary_key=True, default=0, editable=False)
	operation_type = models.IntegerField()
	token = models.UUIDField(default=uuid.uuid4, editable=False)
	phone = models.CharField(max_length=20)
	code_hash = models.CharField(max_length=50)
	client_id = models.CharField(max_length=15)
	create_time = models.DateTimeField(auto_now_add=True)
	sms_id = models.IntegerField()
	expiration_time = models.DateTimeField(auto_now_add=False)
	delivered_time = models.DateTimeField(auto_now_add=False,null=True)
	attempts = models.IntegerField(default=0)
	confirm_time = models.DateTimeField(auto_now_add=False,null=True)
	session_id = models.ForeignKey(SessionModel,on_delete=models.PROTECT,verbose_name='Сессия',null=True)

	def __str__(self):
		return self.client_id

	class Meta:
		verbose_name = 'СМС код'
		verbose_name_plural = 'СМС коды'

class SmsJustifications(models.Model):
	justification_id = models.ForeignKey(Justifications,on_delete=models.PROTECT)
	smscode_id = models.ForeignKey(SmsCodeModel,on_delete=models.PROTECT,verbose_name='Сессия')

	def __str__(self):
		return self.justification_id

	class Meta:
		verbose_name = 'СМС одобрения'
		verbose_name_plural = 'СМС одобрений'