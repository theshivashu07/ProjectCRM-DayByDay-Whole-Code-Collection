from django.shortcuts import render,redirect
from django.http import HttpResponse
from theGuest.models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from theGuest.models import AssignProjectToProjectManagerByMyadmin,AssignProjectToDeveloperByProjectManager
from theGuest.models import ActiveAdmin


def index(request):
	return render(request,"proManager/index.html");


'''
def ActiveAdminMethod(request,val):
	return render(request,"proManager/index.html",{"pmID":val["pmID"],"pmName":val["pmName"]});
	
def logout(request):
	devsvalue=ActiveAdmin.objects.all();
	for i in devsvalue:
		if(i.) 
'''


