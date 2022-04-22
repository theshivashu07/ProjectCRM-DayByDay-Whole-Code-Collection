from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return render(request,"myAdmin/index.html");

def blogentires(request):
	return render(request,"myAdmin/blogentires.html");

def contactus(request):
	return render(request,"myAdmin/contactus.html");

def featured(request):
	return render(request,"myAdmin/featured.html");

def presentation(request):
	return render(request,"myAdmin/presentation.html");

def recentwork(request):
	return render(request,"myAdmin/recentwork.html");







