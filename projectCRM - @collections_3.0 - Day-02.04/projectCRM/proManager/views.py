from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"proManager/index.html");

def shortcodesmethod(request):
	return render(request,"proManager/shortcodes.html");

def simplepagemethod(request):
	return render(request,"proManager/simplepage.html");


