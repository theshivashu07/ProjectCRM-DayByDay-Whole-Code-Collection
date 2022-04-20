from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"theGuest/index.html");

def workprocess(request):
	return render(request,"theGuest/workprocess.html");

def aboutus(request):
	return render(request,"theGuest/aboutus.html");

def contactus(request):
	return render(request,"theGuest/contactus.html");

def login(request):
	return render(request,"theGuest/login.html");

def signup(request):
	return render(request,"theGuest/signup.html");