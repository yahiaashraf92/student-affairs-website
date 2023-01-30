from tokenize import Name
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Student
from django.urls import reverse
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def newHome(request):
    return render(request,"newhome.html")

def home(request):
    return render(request,"home.html")

def edit(request,id):
    return render(request,"edit.html",{
        "student":Student.objects.get(ID = id)
    })

def update(request,id):
    if 'update' in request.POST:
        s = Student.objects.get(ID = id)
        s.Name = request.POST['name']
        s.GPA = request.POST['gpa']
        s.level = request.POST['level']
        s.mail = request.POST['mail']
        s.phone = request.POST['phone']
        id = str(id)
        s.Gender = request.POST[id]
        s.status = request.POST["A"+id]
        s.save()
    else:
        student = Student.objects.get(ID=id)
        student.delete()
    return HttpResponseRedirect(reverse('view'))


def add(request):
    if request.method == "GET":
        return render(request,"addStudent.html")
    else:
        
        name = request.POST['name']
        id = request.POST['id']

        if Student.objects.filter(ID = id):
            messages.error(request,'The ID is already exist')
            return HttpResponseRedirect(reverse('add'))

        gpa = request.POST['gpa']
        levels = request.POST['level']
        mails = request.POST['mail']
        phones = request.POST['phone']
        birthDate = request.POST['birthData']
        gender = request.POST['gender']
        stat = request.POST['status']
        if 'Departments' in request.POST:
            department = request.POST['Departments']
            student = Student(Name=name, ID = id, GPA = gpa, level = levels, mail = mails, phone = phones, dep = department, Gender = gender, status = stat, birth = birthDate)
            student.save()
            return render(request,"addStudent.html")
        else :
            student = Student(Name=name, ID = id, GPA = gpa, level = levels, mail = mails, phone = phones, Gender = gender, status = stat, birth = birthDate)
            student.save()
            return render(request,"addStudent.html")

def view(request):
    return render(request,"view.html",{
        "students" : Student.objects.all()
    })

"""def delete(request):
    id = request.POST['id']
    student = Student.objects.get(ID=id)
    student.delete()
    return HttpResponseRedirect(reverse('view'))
"""
def assign(request):
    id = request.POST['searchid']
    student = Student.objects.get(ID = id)
    if student.level == 3:
        return render(request,"assign.html",{
            "student":Student.objects.get(ID = id)
        })
    else:
        messages.error(request,'The Student is not in level 3')
        return HttpResponseRedirect(reverse('view'))

def assigndep(request,id):
    student = Student.objects.get(ID = id)
    student.dep = request.POST['dep']
    student.save()
    return HttpResponseRedirect(reverse('view'))

def activeStudents(request):
    name = request.POST['searchname']
    return render(request,"activeStudents.html",{
        "students" : Student.objects.filter(Name__startswith=name)
    })

@csrf_protect
def changeActive(request):
    data = json.loads(request.body)
    student = Student.objects.get(ID = data["Ident"])
    student.status = data["stat"]
    student.save()
    return HttpResponse("done")