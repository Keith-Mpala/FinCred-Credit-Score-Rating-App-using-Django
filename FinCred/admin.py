from django.contrib import admin
from .models import PersonalDetails, EmploymentInfor, CreditInfor

# Register your models here.

admin.site.register(PersonalDetails)
admin.site.register(EmploymentInfor)
admin.site.register(CreditInfor)