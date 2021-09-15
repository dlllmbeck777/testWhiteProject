from django.db import models
from datetime import datetime

class SessionModel(models.Model):
	session_id = models.AutoField(primary_key=True)
	session = models.CharField(max_length=64)
	create_time = models.DateTimeField(auto_now_add=True)
	expiration_time = models.DateTimeField(auto_now_add=False)
	auth_type = models.IntegerField(null=True)
	justification_id = models.ForeignKey('Justifications',on_delete=models.PROTECT
			,blank=True, null=True,related_name='session_justification_id')

	def __str__(self):
		return self.session

	class Meta:
		verbose_name = 'Сессия'
		verbose_name_plural = 'Сессий'

class Justifications(models.Model):
	justifications_id = models.IntegerField(primary_key=True, default=0, editable=False)
	justification_type = models.IntegerField()

	def __str__(self):
		return self.justifications_id

	class Meta:
		verbose_name = 'Одобрения'
		verbose_name_plural = 'Одобрений'

class PersonPage(models.Model):
	client_id = models.AutoField(primary_key=True)
	iin = models.CharField(max_length=12)
	phone = models.CharField(max_length=20)
	password_hash = models.CharField(max_length=64)
	surname = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	patronimyc = models.CharField(max_length=100,null=True)
	session_id = models.ForeignKey(SessionModel,on_delete=models.CASCADE,null=True,related_name='person_session_id')
	justification_id = models.ForeignKey(Justifications,on_delete=models.CASCADE,null=True,related_name='person_justification_id')
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now_add=False)


	def __str__(self):
		return self.iin

	class Meta:
		verbose_name = 'ИИН'
		verbose_name_plural = 'ИИН'

class Leads(models.Model):
	lead_id = models.AutoField(primary_key=True)
	iin = models.CharField(max_length=12)
	phone = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now_add=False)
	session_id = models.ForeignKey(SessionModel,on_delete=models.PROTECT,null=True,related_name='lead_session_id')
	personal_data_success = models.BooleanField()

	def __str__(self):
		return self.iin

	class Meta:
		verbose_name = 'ИИН Lead'
		verbose_name_plural = 'ИИН Leads'

class PersonBiometrics(models.Model):
	clientBiometric_id = models.IntegerField(primary_key=True)
	client_id = models.ForeignKey(PersonPage,on_delete=models.PROTECT,null=True)

	def __str__(self):
		return self.clientBiometric_id

	class Meta:
		verbose_name = 'Биометрия'
		verbose_name_plural = 'Биометрия'