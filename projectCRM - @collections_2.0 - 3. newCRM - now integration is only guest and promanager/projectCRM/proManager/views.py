from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"proManager/index.html");

def blogentires(request):
	return render(request,"proManager/blogentires.html");

def contactus(request):
	return render(request,"proManager/contactus.html");

def featured(request):
	return render(request,"proManager/featured.html");

def presentation(request):
	return render(request,"proManager/presentation.html");

def recentwork(request):
	return render(request,"proManager/recentwork.html");





