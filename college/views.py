from django.shortcuts import render, get_object_or_404, redirect
from .models import StudentProfile
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import StudentForm


def student_list(request):
    students = StudentProfile.objects.all()
    # page = request.GET.get.
    context = {
        "students": students
    }
    return render(request, 'college/student_list.html', context)

def student_add(request):
    #if not request.user.is_superuser:
    #    raise Http404
    form = StudentForm(request.POST or None)
    #user = Event.objects.get(id=1)
    student = StudentProfile.objects.all()
    print(student)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.student = student
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/college/hp/')
    context = {
        "form": form,
        "title": "Add Student"
    }
    return render(request, "college/student_add.html", context)

def student_profile(request,id):
    count = StudentProfile.objects.all().count()
    student = StudentProfile.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.student = student
        form.save()
        return HttpResponse("Thanks for registering")
    context = {
    #    "title": event.title,
        "form": form,
        "student": student,
        "students":StudentProfile.objects.filter(id=id),
    }
    return render(request, "college/student_profile.html", context)

def first_page(request):
    context = {
    }
    return render(request,'college/firstpage.html',context)

def college_login(request):
    context = {
    }
    return render(request,'college/collegelogin.html',context)
def student_login(request):
    context = {
    }
    return render(request,'college/studentlogin.html',context)
def railway_login(request):
    context = {
    }
    return render(request,'college/railwaylogin.html',context)
def login(request):
    context = {
    }
    return render(request,'college/login.html',context)
def webcam(request):
    context = {
    }
    return render(request,'college/web.html',context)
