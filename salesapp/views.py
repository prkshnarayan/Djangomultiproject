from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from salesapp.models import Student
from django.contrib import messages
import logging
from .utils.email_utils import send_welcome_email
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

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
        email = request.POST["txtemail"]
        password = request.POST["pswd"]

        if User.objects.filter(Q(username=name) | Q(email=email)).exists():
            return render(request, 'signup.html', {"message": True})
        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            return redirect('login')

    return render(request, 'signup.html')


#
# @login_required
# def add_fun(request):
#     if request.method == "POST":
#         # s1 = Student()
#         # s1.sales_person_id=request.POST["salesperson"]
#         # s1.date_of_join=request.POST["date"]
#         # s1.name=request.POST["txtname"]
#         # s1.email=request.POST["txtemail"]
#         # s1.age=request.POST["txtage"]
#         # s1.place=request.POST["txtplace"]
#         # s1.education=request.POST["txteducation"]
#         # s1.skills=request.POST["txtskills"]
#         # s1.save()
#         # return redirect('display')
#         s1 = Student()
#
#         # Use .get() to safely fetch data from POST
#         s1.sales_person_id = request.POST.get("salesperson")
#         s1.date_of_joining = request.POST.get("date")
#         s1.name = request.POST.get("txtname")
#         s1.email = request.POST.get("txtemail")
#         if Student.objects.filter(email=s1.email).exists():
#             return render(request, 'addstudent.html', {
#                 "message": True
#             })
#         s1.age = request.POST.get("txtage")
#         s1.place = request.POST.get("txtplace")
#         s1.education = request.POST.get("txteducation")
#         s1.skills = request.POST.get("txtskills")
#
#         try:
#             s1.save()
#         except ValidationError as e:
#             return render(request, 'addstudent.html', {
#                 "message": str(e)
#             })
#
#         # Redirect to the 'display' view
#         return redirect('display')
#     else:
#         if status:
#             salesdata = User.objects.all()
#         else:
#             salesdata = User.objects.filter(username=exist_user)
#         return render(request, 'addstudent.html', {"salesdata": salesdata})


@login_required
def add_fun(request):
    if request.method == "POST":
        # Initialize form data dictionary for potential reuse
        form_data = {
            'salesperson': request.POST.get("salesperson"),
            'date': request.POST.get("date"),
            'txtname': request.POST.get("txtname"),
            'txtemail': request.POST.get("txtemail"),
            'txtage': request.POST.get("txtage"),
            'txtplace': request.POST.get("txtplace"),
            'txteducation': request.POST.get("txteducation"),
            'txtskills': request.POST.get("txtskills"),
        }

        # Validate required fields
        required_fields = ['txtname', 'txtemail', 'date']
        for field in required_fields:
            if not form_data[field]:
                return render(request, 'addstudent.html', {
                    "salesdata": User.objects.all(),
                    "form_data": form_data,
                    "error_message": f"{field.replace('txt', '')} is required"
                })

        # Check for duplicate email
        if Student.objects.filter(email=form_data['txtemail']).exists():
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "form_data": form_data,
                "error_message": "Email already exists"
            })

        try:
            # Create and save student
            student = Student(
                sales_person_id=form_data['salesperson'],
                date_of_joining=form_data['date'],
                name=form_data['txtname'],
                email=form_data['txtemail'],
                age=form_data['txtage'],
                place=form_data['txtplace'],
                education=form_data['txteducation'],
                skills=form_data['txtskills']
            )
            student.save()

            # Send welcome email
            try:
                if send_welcome_email(student):
                    messages.success(request, "Student added successfully and welcome email sent!")
                else:
                    messages.warning(request, "Student added but email failed to send")
            except Exception as email_error:
                logger.error(f"Email sending error: {str(email_error)}")
                messages.warning(request, "Student added but email system encountered an error")

            return redirect('display')

        except ValidationError as e:
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "form_data": form_data,
                "error_message": str(e)
            })
        except Exception as e:
            logger.error(f"Error adding student: {str(e)}")
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "form_data": form_data,
                "error_message": "An unexpected error occurred"
            })
    else:
        salesdata = User.objects.all() if request.user.is_superuser else User.objects.filter(username=request.user.username)
        return render(request, 'addstudent.html', {
            "salesdata": salesdata,
            "form_data": None
        })


@login_required
def home_fun(request):
    return render(request, 'home.html', {
        "existuser": request.user,
        "status": request.user.is_superuser
    })


@login_required
def display_fun(request):
    is_admin = request.user.is_superuser
    if is_admin:
        studentdata = Student.objects.all()
    else:
        studentdata = Student.objects.filter(sales_person=request.user)
    return render(request, 'display.html', {
        "studentdata": studentdata,
        "status": is_admin
    })


@login_required
def logout_fun(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")


# @login_required
# def update_fun(request, id):
#     salesdata = User.objects.all()
#     s1 = Student.objects.get(id=id)
#     if request.method == "POST":
#         email = request.POST.get("txtemail")
#
#         if Student.objects.exclude(id=id).filter(email=email).exists():
#             return render(request, 'addstudent.html', {
#                 "salesdata": salesdata,
#                 "student": s1,
#                 "message": True
#             })
#
#         s1.sales_person_id = request.POST.get("salesperson")
#         s1.date_of_join = request.POST.get("date")
#         s1.name = request.POST.get("txtname")
#         # s1.email = request.POST.get("txtemail")
#         s1.email = email
#         s1.age = request.POST.get("txtage")
#         s1.place = request.POST.get("txtplace")
#         s1.education = request.POST.get("txteducation")
#         s1.skills = request.POST.get("txtskills")
#         try:
#             s1.save()
#         except ValidationError as e:
#             return render(request, 'addstudent.html', {
#                 "salesdata": salesdata,
#                 "student": s1,
#                 "message": str(e)
#             })
#         # s1.save()
#         return redirect('display')
#     else:
#         return render(request, 'addstudent.html', {"salesdata": salesdata, "student": s1})

@login_required
def update_fun(request, id):
    if request.method == "POST":
        # Initialize form data dictionary for potential reuse
        form_data = {
            'salesperson': request.POST.get("salesperson"),
            'date': request.POST.get("date"),
            'txtname': request.POST.get("txtname"),
            'txtemail': request.POST.get("txtemail"),
            'txtage': request.POST.get("txtage"),
            'txtplace': request.POST.get("txtplace"),
            'txteducation': request.POST.get("txteducation"),
            'txtskills': request.POST.get("txtskills"),
        }

        # Validate salesperson is a number (not "disabled selected")
        try:
            salesperson_id = int(form_data['salesperson'])
        except (ValueError, TypeError):
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "student": Student.objects.get(id=id),
                "form_data": form_data,
                "error_message": "Please select a valid salesperson"
            })

        # Validate required fields
        required_fields = ['txtname', 'txtemail', 'date']
        for field in required_fields:
            if not form_data[field]:
                return render(request, 'addstudent.html', {
                    "salesdata": User.objects.all(),
                    "student": Student.objects.get(id=id),
                    "form_data": form_data,
                    "error_message": f"{field.replace('txt', '')} is required"
                })

        # Check for duplicate email (excluding current student)
        if Student.objects.exclude(id=id).filter(email=form_data['txtemail']).exists():
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "student": Student.objects.get(id=id),
                "form_data": form_data,
                "error_message": "Email already exists"
            })

        try:
            # Get and update student
            student = Student.objects.get(id=id)
            student.sales_person_id = salesperson_id
            student.date_of_joining = form_data['date']
            student.name = form_data['txtname']
            student.email = form_data['txtemail']
            student.age = form_data['txtage']
            student.place = form_data['txtplace']
            student.education = form_data['txteducation']
            student.skills = form_data['txtskills']
            student.save()

            # Send email notification (using existing send_welcome_email)
            try:
                if send_welcome_email(student):  # Using your existing function as-is
                    messages.success(request, "Student updated successfully and notification email sent!")
                else:
                    messages.warning(request, "Student updated but email failed to send")
            except Exception as email_error:
                logger.error(f"Email sending error: {str(email_error)}")
                messages.warning(request, "Student updated but email system encountered an error")

            return redirect('display')

        except ValidationError as e:
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "student": Student.objects.get(id=id),
                "form_data": form_data,
                "error_message": str(e)
            })
        except Exception as e:
            logger.error(f"Error updating student: {str(e)}")
            return render(request, 'addstudent.html', {
                "salesdata": User.objects.all(),
                "student": Student.objects.get(id=id),
                "form_data": form_data,
                "error_message": "An unexpected error occurred"
            })
    else:
        salesdata = User.objects.all() if request.user.is_superuser else User.objects.filter(username=request.user.username)
        student = Student.objects.get(id=id)
        return render(request, 'addstudent.html', {
            "salesdata": salesdata,
            "student": student
        })


@login_required
def delete_fun(request, id):
    student_delete = Student.objects.get(id=id)
    student_delete.delete()
    return redirect('display')


@login_required
def employee_fun(request):
    employee = User.objects.all()
    return render(request, 'employee.html', {
        'employee': employee,
        'status': request.user.is_superuser
    })
