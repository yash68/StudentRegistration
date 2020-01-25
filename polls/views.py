from django.shortcuts import render, HttpResponse, redirect
import time
# Create your views here.
from .forms import SampleForm, StudentForm, UserForm
from .models import Student
#from django.urls import reverse
from django.contrib import auth

def index(request):
	obj = SampleForm()
	d = {'name':"Ram",'time':time.ctime(),'form':obj}
	return render(request, 'index.html',d)

def addstudent(request):
	if request.method=="POST":
		form = StudentForm(request.POST,request.FILES)
		print(form)
		if form.is_valid():
			form.save()
			return HttpResponse("Thank You")
	else:
		form = StudentForm()
	return render(request, 'student.html', {'form':form})

def homepage(request):
	return render(request, 'home.html')

def showstudent(request):
	data = Student.objects.all()
	return render(request, 'show.html', {'students':data})


def deletestudent(request,id):
	d = Student.objects.get(id=id)
	d.delete()	
	return redirect('/show')

def updatestudent(request,id):
	data = Student.objects.get(id=id)
	form = StudentForm(request.POST, instance=data)
	if form.is_valid():
		form.save()
		return render(request, 'home.html')
	return render(request, 'edit.html', {'student':data})
#ndtv Republic
def registration(request):
	if request.method=="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Registration Success")		
	else:		
		form = UserForm()
	return render (request,"registration.html",{"form":form})

def loginpage(request):
	return render(request, 'login.html')

def auth_view(request):
   
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        
        return HttpResponse('Logged in')
    else:
        return HttpResponse('Invalid username and password')   