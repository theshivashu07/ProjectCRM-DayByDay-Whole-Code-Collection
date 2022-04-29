from django.shortcuts import render
from django.http import HttpResponse
from theGuest.models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager




def index(request):
	return render(request,"myAdmin/trials/index.html");

def RecruitDeveloperMethod(request):
	if request.method=="POST":
		values=RecruitDeveloper(FullName=request.POST["txtfname"],Age=request.POST["txtage"],MoblileNo=request.POST["txtmobileno"],EmailId=request.POST["txtemail"],WorkExperience=request.POST["txtworkexp"],Specialization=request.POST["txtcategory"],Address=request.POST["txtaddress"],UserId=request.POST["txtuname"],Password=request.POST["txtpassword"])
		values.save()
		return render(request,"myAdmin/Collections/RecruitDeveloper.html",{"result":"_____'"+values.FullName+"' Registered, as Developer._____"})
	value=WorksOnLanguage.objects.all();
	return render(request,"myAdmin/Collections/RecruitDeveloper.html",{"values":value});

def RecruitHrMethod(request):
	if request.method=="POST":
		values=RecruitHr(FullName=request.POST["txtfname"],Age=request.POST["txtage"],MoblileNo=request.POST["txtmobileno"],EmailId=request.POST["txtemail"],WorkExperience=request.POST["txtworkexp"],Specialization=request.POST["txtcategory"],Address=request.POST["txtaddress"],UserId=request.POST["txtuname"],Password=request.POST["txtpassword"])
		values.save()
		return render(request,"myAdmin/Collections/RecruitHr.html",{"result":"_____'"+values.FullName+"' Registered, as HR._____"})
	value=WorksOnLanguage.objects.all();
	return render(request,"myAdmin/Collections/RecruitHr.html",{"values":value});

def RecruitDeveloperAsProjectManagerMethod(request): 
	if request.method=="POST":
		myID=request.POST["txtcategory"]
		DevsData=RecruitDeveloper.objects.all();
		for data in DevsData:
			if(int(myID)==data.id):
				values=RecruitDeveloperAsProjectManager(FullName=data.FullName,UserId=data.UserId,Password=data.Password)
				values.save()
				return render(request,"myAdmin/Collections/RecruitHr.html",{"result":"_____'"+values.FullName+"' promoted as proManager._____"});
		return render(request,"myAdmin/Collections/RecruitHr.html",{"result":"_____'"+values.FullName+"' promoted as proManager._____"});
	value=RecruitDeveloper.objects.all();
	return render(request,"myAdmin/Collections/RecruitDeveloperAsProjectManager.html",{"values":value});







'''
FullName = Age = MoblileNo = EmailId = WorkExperience = Address = UserId =  Password = 
def RecruitDevelopers(request):
	if request.method=="POST":
		checked=request.POST["txtemail"];
		k=0
		for i in checked:
			if(i=='@'):
				break;
			k+=1
		UserPass=checked[0:k];
		done=RecruitDeveloper(fullName=request.POST["txtfname"],emailId=request.POST["txtemail"],userId1=UserPass,password1=UserPass);
		done.save();
		return render(request,"myAdmin/collections/HiringDevs.html",{"msg1":"You hiring "+done.fullName+", as Developer.","msg2":"and its User Id and Password is same,","msg3":"and it is:  '"+UserPass+"'.","txtfname":done.fullName,"txtemail":done.emailId});
	return render(request,"myAdmin/collections/HiringDevs.html");
'''
