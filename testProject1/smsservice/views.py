from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import SmsCodeModel
from .forms import PersonLeadForm
from formpage1.models import SessionModel, Leads, PersonPage
from .smscoderender import smsServiceRequest, egovServiceRequest
import random
from django.utils import timezone

@csrf_exempt
def smscodegenerate(request):
	form = PersonLeadForm(request.POST or None)
	print()
	print('SMS request:',request.session.session_key)
	if request.method == 'POST':		
		if form.is_valid():			
			print(' ++++++++ ++++++++ ',form.data.get('sms_code'))
			session_id = SessionModel.objects.filter(session=request.session.session_key)[0].session_id
			iin = Leads.objects.filter(session_id=session_id)[0].iin
			phone = Leads.objects.filter(session_id=session_id)[0].phone
			sendsms = smsServiceRequest(iin,phone,form.data.get('sms_code'))
			print('Result sms: ',sendsms.get())
			egovservice = egovServiceRequest(iin)
			resultegov = egovservice.getResult()
			print('Result egov: ',resultegov)
			modelPage = PersonPage()
			modelPage.iin = resultegov['iin']
			modelPage.phone = resultegov['phone']
			modelPage.password_hash = None
			modelPage.surname = resultegov['surname']
			modelPage.name = resultegov['name']
			modelPage.patronimyc = resultegov['patronimyc']
			modelPage.session_id = session_id
			modelPage.justification_id = None
			modelPage.create_time = timezone.now()
			modelPage.update_time = timezone.now()
			modelPage.save()
	return render(request,'smspage2.html',{'form':form})

def smsresultshow(request,smscode7):
	return render(request,'resultSmsCode.html',{'smscode7':smscode7})
