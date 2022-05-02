from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from .models import AssignProjectToProjectManagerByMyadmin

def index(request):
	return render(request,"theGuest/index.html");

def workprocess(request):
	return render(request,"theGuest/workprocess.html");

def aboutus(request):
	return render(request,"theGuest/aboutus.html");

def contactus(request):
	return render(request,"theGuest/contactus.html");



def checkOnIt(SearchId,InSearch):
	for data in InSearch:
		if(SearchId==data.id):
			return data;
def loginMethod(request):
	if request.method=="POST":
		haved=str(request.POST["fromwhere"])
		UsernameorEmail=request.POST["txtname"];
		Password=request.POST["txtpassword"]
		if(haved=="MyAdmin"):
			if((UsernameorEmail=="shishu07@gmail.com" or UsernameorEmail=="shishu07") and Password=="shishu07"):
				return redirect("/myadmin");
		elif(haved=="ProjectManager"):
			pmvalue=RecruitDeveloperAsProjectManager.objects.all();
			devsvalue=RecruitDeveloper.objects.all();
			lst=[];
			for data in pmvalue:
				lst.append(checkOnIt(int(data.DevsId),devsvalue));
			for data in lst:
				if((UsernameorEmail==data.EmailId or UsernameorEmail==data.UserId) and Password==data.Password):
					return redirect("/promanager");
		return render(request,"theGuest/login.html",{"fromwhere":haved,"passmsg":"_____Invalied Data_____"});
	fromwhere=request.GET["have"];
	return render(request,"theGuest/login.html",{"fromwhere":fromwhere});


