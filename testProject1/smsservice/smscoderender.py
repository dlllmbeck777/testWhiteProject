from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
import random

def smscoderender(request):
	smscode7 = ''.join([str(random.randint(1,9)) for i in range(4)])
	return HttpResponseRedirect(reverse('smsresultshow', kwargs={'smscode7': smscode7}))
	# return redirect('smsresultshow', {'smscode7': smscode7})
	# return render(request,'resultSmsCode.html',{'smscode7':smscode7})
	# return reverse('smsresultshow', kwargs={'smscode7': smscode7})

class smsServiceRequest:
	def __init__(self,iin,phone,code):
		self.iin = iin
		self.phone = phone
		self.code = code

	def get(self):
		resultDict = {'iin':self.iin,'phone':self.phone,'code':self.code,'status':'sended'}
		return resultDict

	def getStatus(self):
		return 'Delivered'

class egovServiceRequest:
	def __init__(self,iin):
		self.iin = iin

		self.createInfo(iin)

	def getResult(self):
		resultJson = {'iin':self.iin,
					'surname':self.surname,
					'name':self.name,
					'patronimyc':self.patronimyc,
					'phone':self.phone}
		return resultJson

	def createInfo(self,iin):
		print('create Info: ',iin)
		if iin=='900710000111':
			self.surname = 'Stone'
			self.name = 'Novak'
			self.patronimyc = 'Mike'
			self.phone = '7778889900'
		elif iin=='999988887777':
			self.surname = 'John'
			self.name = 'Stuard'
			self.patronimyc = None
			self.phone = '7776665544'
		else:
			self.surname = None
			self.name = None
			self.patronimyc = None
			self.phone = None


