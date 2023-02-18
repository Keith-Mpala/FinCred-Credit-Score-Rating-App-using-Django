# from tkinter import CASCADE
from tkinter import Menu, CASCADE
from django.db import models
import _tkinter

# Create your models here.
class PersonalDetails(models.Model):
    username = models.TextField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField()
    phone_number = models.IntegerField()


class EmploymentInfor(models.Model):
    employer = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    contract = models.CharField(max_length=80)
    years_at_employment = models.IntegerField()
    person = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE, default=25)


class CreditInfor(models.Model):
    no_of_creditcards = models.IntegerField()
    annual_gross_salary = models.IntegerField()
    overdueaccounts = models.IntegerField()
    total_credit_balances = models.IntegerField()
    new_credit_cards = models.IntegerField()
    first_creditloan = models.IntegerField()
    total_credit_limit = models.IntegerField()
    bankruptcy = models.BooleanField()
    employment = models.ForeignKey(EmploymentInfor, on_delete=models.CASCADE, default= 39)

    

    
