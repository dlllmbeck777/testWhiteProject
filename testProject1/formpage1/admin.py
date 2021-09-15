from django.contrib import admin
from .models import SessionModel, Justifications, PersonPage, Leads, PersonBiometrics

# Register your models here.
admin.site.register(SessionModel)
admin.site.register(Justifications)
admin.site.register(PersonPage)
admin.site.register(Leads)
admin.site.register(PersonBiometrics)


