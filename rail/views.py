from django.shortcuts import render, get_object_or_404, redirect
from college.models import StudentProfile
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import StudentForm


def student_list(request):
    students = StudentProfile.objects.all()
    # page = request.GET.get.
    context = {
        "students": students
    }
    return render(request, 'rail/student_list.html', context)

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
        return HttpResponseRedirect('Thanks')
    context = {
        "form": form,
        "title": "Add Student"
    }
    return render(request, "rail/student_add.html", context)

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
    return render(request, "rail/student_profile.html", context)

def student_delete(request,id):
    student = StudentProfile.objects.filter(id=id)
    if request.POST:
        student.delete()
        return redirect("rail/list")
    context = {
        "title": "Delete",
        "student":student,
    }
    return render(request, "rail/rail_delete.html", context)
