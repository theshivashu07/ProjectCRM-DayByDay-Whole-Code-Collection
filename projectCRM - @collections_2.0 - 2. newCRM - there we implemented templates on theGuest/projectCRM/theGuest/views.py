from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"theGuest/index.html");

def aboutus(request):
	return render(request,"theGuest/aboutus.html");

def blogentries(request):
	return render(request,"theGuest/blogentries.html");

def contactus(request):
	return render(request,"theGuest/contactus.html");

def pricingplans(request):
	return render(request,"theGuest/pricingplans.html");

def testimonials(request):
	return render(request,"theGuest/testimonials.html");

def workprocess(request):
	return render(request,"theGuest/workprocess.html");
