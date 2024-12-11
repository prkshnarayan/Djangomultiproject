from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from salesapp.models import Student


# Create your views here.
# def login_fun(request):
#     if request.method=="POST":
#         name=request.POST["txtname"]
#         password=request.POST["pswd"]
#         global exist_user
#         exist_user=authenticate(request,username=name,password=password)
#         global status
#         if exist_user is not None:
#             if exist_user.is_superuser:
#                 status="admin"
#                 return render(request,'home.html',{"existuser":exist_user,"status":status})
#
#             elif exist_user.is_authenticated:
#                 status="sales"
#                 return render(request,'home.html',{"existuser":exist_user,"status":status})
#         else:
#             return render(request, 'login.html',{"message":True})
#
#     return render(request,'login.html')


def signup(request):
    if request.method == "POST":
        name = request.POST["txtname"]
        email = request.POST["txtmail"]
        password = request.POST["pswd"]

        if User.objects.filter(Q(username=name) | Q(email=email)).exists():
            return render(request, 'signup.html', {"message": True})
        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            return redirect('login')

    return render(request, 'signup.html')


@login_required
def add_fun(request):
    if request.method == "POST":
        # s1 = Student()
        # s1.sales_person_id=request.POST["salesperson"]
        # s1.date_of_join=request.POST["date"]
        # s1.name=request.POST["txtname"]
        # s1.email=request.POST["txtemail"]
        # s1.age=request.POST["txtage"]
        # s1.place=request.POST["txtplace"]
        # s1.education=request.POST["txteducation"]
        # s1.skills=request.POST["txtskills"]
        # s1.save()
        # return redirect('display')
        s1 = Student()

        # Use .get() to safely fetch data from POST
        s1.sales_person_id = request.POST.get("salesperson")
        s1.date_of_joining = request.POST.get("date")
        s1.name = request.POST.get("txtname")
        s1.email = request.POST.get("txtemail")
        if Student.objects.filter(email=s1.email).exists():
            return render(request, 'addstudent.html', {
                "message": True
            })
        s1.age = request.POST.get("txtage")
        s1.place = request.POST.get("txtplace")
        s1.education = request.POST.get("txteducation")
        s1.skills = request.POST.get("txtskills")

        try:
            s1.save()
        except ValidationError as e:
            return render(request, 'addstudent.html', {
                "message": str(e)
            })

        # Redirect to the 'display' view
        return redirect('display')
    else:
        if status:
            salesdata = User.objects.all()
        else:
            salesdata = User.objects.filter(username=exist_user)
        return render(request, 'addstudent.html', {"salesdata": salesdata})


@login_required
def home_fun(request):
    global exist_user
    exist_user = request.user
    global status
    status = exist_user.is_superuser
    return render(request, 'home.html', {"existuser": exist_user, "status": status})


@login_required
def display_fun(request):
    if status:
        studentdata = Student.objects.all()
    else:
        studentdata = Student.objects.filter(sales_person=exist_user)
    return render(request, 'display.html', {"studentdata": studentdata, "status": status})


@login_required
def logout_fun(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")


@login_required
def update_fun(request, id):
    salesdata = User.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method == "POST":
        email = request.POST.get("txtemail")

        if Student.objects.exclude(id=id).filter(email=email).exists():
            return render(request, 'addstudent.html', {
                "salesdata": salesdata,
                "student": s1,
                "message": True
            })

        s1.sales_person_id = request.POST.get("salesperson")
        s1.date_of_join = request.POST.get("date")
        s1.name = request.POST.get("txtname")
        # s1.email = request.POST.get("txtemail")
        s1.email = email
        s1.age = request.POST.get("txtage")
        s1.place = request.POST.get("txtplace")
        s1.education = request.POST.get("txteducation")
        s1.skills = request.POST.get("txtskills")
        try:
            s1.save()
        except ValidationError as e:
            return render(request, 'addstudent.html', {
                "salesdata": salesdata,
                "student": s1,
                "message": str(e)
            })
        # s1.save()
        return redirect('display')
    else:
        return render(request, 'addstudent.html', {"salesdata": salesdata, "student": s1})


@login_required
def delete_fun(request, id):
    student_delete = Student.objects.get(id=id)
    student_delete.delete()
    return redirect('display')


@login_required()
def employee_fun(request):
    employee = User.objects.all()
    # if status:
    return render(request, 'employee.html', {'employee': employee, 'status': status})
    # else:
    #     return redirect('display')
