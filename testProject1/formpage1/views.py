from django.shortcuts import render, redirect
from formpage1.forms import PersonLeadForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from formpage1.models import SessionModel, Justifications, PersonPage, Leads, PersonBiometrics
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import calendar
import time
import random
from django.utils import timezone
# Create your views here.

@csrf_exempt
def signupform(request):
    form = PersonLeadForm(request.POST or None)
    # print("Request: -----> ",dir(request))
    if request.method == 'POST':
        if form.is_valid():
            print("Form: -----> ",form.data.get('iin'))
            # ----- call models -----
            checkLeads = Leads()
            sessionClass = SessionModel()
            iin = form.data.get('iin')
            phone = form.data.get('phone')
            print('Formpage1 IIN: ',iin,' PHONE: ',phone)
            # ------- creating if not exist ---------
            if Leads.objects.all().filter(iin=iin).count()==0:
                print('----- creating session -----')
                # ----- creating session -----
                request.session.create() 
                sessionClass.session = request.session.session_key
                sessionClass.create_time = datetime.now()
                sessionClass.expiration_time = request.session.get_expiry_date()       
                sessionClass.save()
                model = form.save(commit=False)
                model.create_time = timezone.now()
                model.update_time = timezone.now()
                model.personal_data_success = True if form.data.get('is_gathering')=='on' else False
                model.session_id = SessionModel.objects.all().filter(session=request.session.session_key)[0]
                model.save()
            else:
                lastExpireDate = SessionModel.objects.filter(
                    session_id = max([i.session_id.session_id for i in Leads.objects.all().filter(iin=iin)])
                        )[0].expiration_time

                if lastExpireDate<=timezone.now():
                    print('---------- create and update session key -----------')
                    # ---------- create and update session key -----------
                    request.session.create()
                    sessionClass = SessionModel()
                    sessionClass.session = request.session.session_key
                    sessionClass.create_time = datetime.now()
                    sessionClass.expiration_time = request.session.get_expiry_date()       
                    sessionClass.save()
                    Leads.objects.all().filter(iin=iin).update(session_id=SessionModel.objects.all().filter(session=request.session.session_key)[0])
            if "+" in phone:
                phone = phone[1:]
            return redirect('smspage')

    return render(request, 'formPage1.html', {'form': form})
