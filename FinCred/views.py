from django.http.response import HttpResponse
from django.shortcuts import redirect, render
#from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from FinCred.models import EmploymentInfor, PersonalDetails, CreditInfor


# Create your views here.
def home(request):
    return render(request, "FinCred/index.html")        


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        ins = PersonalDetails(username=username, first_name=fname, last_name=lname, email_address=email, phone_number=phone)
        ins.save()
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        if len(phone) > 9:
            messages.error(request, "Phone number must be 9 characters")
            return redirect('home')

        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')
        
    return render(request, "FinCred/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'FinCred/index.html', {'fname':fname})

        else:
            messages.error(request, 'Bad credetials')
            return redirect('home')

    return render(request, "FinCred/signin.html")


def employment_details(request):
    if request.method == "POST":
        employer = request.POST.get('employer')
        sector = request.POST.get('sector')
        contract = request.POST.get('contract')
        years = request.POST.get('years')

        ins = EmploymentInfor(employer=employer, sector=sector, contract=contract, years_at_employment=years)
        ins.save()

        return render(request, 'FinCred/credit_details.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out succesfully")
    return redirect('home')


def credit_details(request):
    if request.method == "POST":
        creditcards = request.POST.get('creditcards')
        grosssalary = request.POST.get('grosssalary')
        overdueaccounts = request.POST.get('overdueaccounts')
        totalbalances = request.POST.get('totalbalances')
        newcards = request.POST.get('newcards')
        firstloan = request.POST.get('firstloan')
        totallimit = request.POST.get('totallimit')
        bankruptcy = request.POST.get('bankruptcy')

        ins = CreditInfor(no_of_creditcards=creditcards, annual_gross_salary=grosssalary , overdueaccounts=overdueaccounts, total_credit_balances=totalbalances, 
        new_credit_cards=newcards, first_creditloan=firstloan, total_credit_limit=totallimit,bankruptcy=bankruptcy  )
        ins.save()

    
    
    creditcards1 = int(request.POST.get("creditcards"))
    grosssalary1 = int(request.POST.get('grosssalary'))
    overdueaccounts1 = int(request.POST.get('overdueaccounts'))
    totalbalances1 = int(request.POST.get('totalbalances'))
    newcards1 = int(request.POST.get('newcards'))
    firstloan1 = int(request.POST.get('firstloan'))
    totallimit1 = int(request.POST.get('totallimit'))
    bankruptcy1 = request.POST.get('bankruptcy')

    if creditcards1 < 2:
        val1 = int(0.1 * 850 * 0.95)
    elif 2 <= creditcards1 < 4:
        val1 = int(0.1 * 850 * 1)
    elif 4 <= creditcards1 < 6:
        val1 = int(0.1 * 850 * 0.9)
    elif 6 <= creditcards1 < 8:
        val1 = int(0.1 * 850 * 0.8)
    else:
        val1 = int(0.1 * 850 * 0.6)

    if grosssalary1 < 20000:
        val2 = int(0.2 *850 * 0.8)
    elif 20000 <= grosssalary1 < 40000:
        val2 = int(0.2 * 850 * 0.85)
    elif 40000 <= grosssalary1 < 70000:
        val2 = int(0.2 * 850 * 0.9)
    elif 70000 <= grosssalary1 < 100000:
        val2 = int(0.2 * 850 * 0.95)
    elif 100000 <= grosssalary1 < 150000:
        val2 = int(0.2 * 850 * 1)
    elif 150000 <= grosssalary1 <= 200000:
        val2 = int(0.2 * 850 * 1.05)
    else:
        val2 = int(0.2 * 850 * 1.1)
    
    if overdueaccounts1 == 0:
        val3 = int(0.2 * 850 * 1)
    elif overdueaccounts1 == 1:
        val3 = int(0.2 * 850 * 0.9)
    elif overdueaccounts1 == 2:
        val3 = int(0.2 * 850 * 0.8)
    elif overdueaccounts1 == 3:
        val3 = int(0.2 * 850 * 0.7)
    elif overdueaccounts1 == 4:
        val3 = int(0.2 * 850 * 0.5)
    elif 4 <= overdueaccounts1 < 6:
        val3 = int(0.2 * 850 * 0.2)
    else:
        val3 = int(0.2 * 850 * 0)

    if totalbalances1 < 2000:
        val4 = int(0.2 * 850 * 1)
    elif 2000 <= totalbalances1 < 5000:
        val4 = int(0.2 * 850 * 0.9)
    elif 5000 <= totalbalances1 < 10000:
        val4 = int(0.2 * 850 * 0.8)
    elif 10000 <= totalbalances1 < 15000:
        val4 = int(0.2 * 850 * 0.7)
    elif 15000 <= totalbalances1 < 20000:
        val4 = int(0.2 * 850 * 0.5)
    elif 20000 <= totalbalances1 < 25000:
        val4 = int(0.2 * 850 * 0.3)
    elif 25000 <= totalbalances1 < 75000:
        val4 = int(0.2 * 850 * 0)
    else:
        val4 = int(0.2 * 850 * -0.1)

    if newcards1 < 2:
        val5 = int(0.1 * 850 * 0.6)
    elif 2 <= newcards1 < 4:
        val5 = int(0.1 * 850 * 1)
    elif 4 <= newcards1 < 6:
        val5 = int(0.1 * 850 * 0.8)
    elif 6 <= newcards1 < 8:
        val5 = int(0.1 * 850 * 0.5)
    elif 8 <= newcards1 < 10:
        val5 = int(0.1 * 850 * 0.4)
    else:
        val5 = int(0.1 * 850 * 0.1)

    if firstloan1 < 3:
        val6 = int(0.1 * 850 * 0.6)
    elif 3 <= firstloan1 < 5:
        val6 = int(0.1 * 850 * 0.7)
    elif 5 <= firstloan1 < 8:
        val6 = int(0.1 * 850 * 0.8)
    elif 8 <= firstloan1 < 10:
        val6 = int(0.1 * 850 * 0.9)
    else:
        val6 = int(0.1 *850 * 1)
    
    if totallimit1 < 10000:
        val7 = int(0.1 * 850 *0.5)
    elif 10000 <= totallimit1 < 15000:
        val7 = int(0.1 *850 * 0.6)
    elif 15000 <= totallimit1 <= 20000:
        val7 = int(0.1 *850 * 0.7)
    elif 20000 <= totallimit1 <= 35000:
        val7 = int(0.1 *850 * 0.8)
    elif 35000 <= totallimit1 <= 55000:
        val7 = int(0.1 *850 * 0.9)
    elif 55000 <= totallimit1 <= 100000:
        val7 = int(0.1 *850 * 1)
    else:
        val7 = int(0.1 * 850 * 1.2)
    
    
    if bankruptcy1 == "True":
        val8 = 0
    else:
        val8 = -100
    

    res = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8
    if res < 350:
        score = 350
    elif bankruptcy1 == "True" and res < 350:
        score = 350
    elif bankruptcy1 == "True" and 350 <= res < 650:
        score = 400
    elif bankruptcy1 == "True" and 650 <= res < 900:
        score = 450
    else:
        score = res
    
    #res = creditcards + grosssalary
    return render(request, "FinCred/creditscore.html", {'result':score})




        