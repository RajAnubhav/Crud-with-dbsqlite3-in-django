from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import *
# Create your views here.

# this function will add and will show all the items


def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()

            # you can also use fm.save()
    else:
        fm = StudentRegistration()

    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# this function will delete


def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# this function will edit and update the data

def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    stud = User.objects.all()
    return render(request, 'enroll/updatestudent.html', {'form': fm, 'id': id})
