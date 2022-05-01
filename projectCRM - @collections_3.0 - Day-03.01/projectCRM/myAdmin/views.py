from django.shortcuts import render,redirect
from django.http import HttpResponse
from theGuest.models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from theGuest.models import AssignProjectToProjectManagerByMyadmin





def index(request):
	return render(request,"myAdmin/index.html");

def editsMethod(request):
	if request.method=="POST":
		haved=str(request.POST["fromwhere"])
		if(haved=="Developer" or haved=="Project Manager"):
			lock=RecruitDeveloper.objects.get(pk=request.POST["txthidden"])
		elif(haved=="HR"):
			lock=RecruitHr.objects.get(pk=request.POST["txthidden"])
		lock.FullName=request.POST["txtfname"]
		lock.Age=request.POST["txtage"]
		lock.MoblileNo=request.POST["txtmobileno"]
		lock.EmailId=request.POST["txtemail"]
		lock.WorkExperience=request.POST["txtworkexp"]
		lock.Specialization=request.POST["txtprojectcategory"]
		lock.Address=request.POST["txtaddress"]
		lock.UserId=request.POST["txtuname"]
		lock.Password=request.POST["txtpassword"]
		lock.save()
		if(haved=="Developer"):
			pmvalue=RecruitDeveloperAsProjectManager.objects.all();
			devsvalue=RecruitDeveloper.objects.all();
			lst=[];
			for data in devsvalue:
				if(checkOnIt(data.id,pmvalue,"showDevelopers")):
					lst.append(data)
			return render(request,"myAdmin/Another/showDevelopers.html",{"result":lst});
		elif(haved=="Project Manager"): 
			pmvalue=RecruitDeveloperAsProjectManager.objects.all();
			devsvalue=RecruitDeveloper.objects.all();
			lst=[];
			for data in pmvalue:
				lst.append(checkOnIt(int(data.DevsId),devsvalue,"showProManager"))
			return render(request,"myAdmin/Another/showProManager.html",{"result":lst});
		elif(haved=="HR"):
			lst=RecruitHr.objects.all();
			return render(request,"myAdmin/Another/showHR.html",{"result":lst});
	value=WorksOnLanguage.objects.all();
	fromwhere=request.GET["var2"]
	if(fromwhere=="Developer" or fromwhere=="Project Manager"):
		data=RecruitDeveloper.objects.get(pk=request.GET["var1"]);
	elif(fromwhere=="Project Manager"):
		val=RecruitDeveloperAsProjectManager.objects.get(pk=request.GET["var1"]);
		Ids=int(val.DevsId);
		data=RecruitDeveloper.objects.get(pk=request.GET[Ids]);
	elif(fromwhere=="HR"):
		data=RecruitHr.objects.get(pk=request.GET["var1"]);
	return render(request,"myAdmin/edits.html",{"value":data,"values":value,"fromwhere":fromwhere});

'''
def editHRMethod(request):
	data=RecruitHr.objects.get(pk=request.GET["q"])
	return render(request,"myAdmin/editDeveloper.html",{"value":data});

def editProjectManagerMethod(request):
	data=RecruitDeveloper.objects.get(pk=request.GET["q"])
	return render(request,"myAdmin/editDeveloper.html",{"value":data});
'''

def deletes(request):
	pass


def checkOnIt(SearchId,InSearch,who):
	if(who=="showDevelopers"):
		for data in InSearch:
			if(SearchId==int(data.DevsId)):
				return False;
		else:
			return True;
	elif(who=="showProManager"):
		for data in InSearch:
			if(SearchId==data.id):
				return data;

def showDevelopers(request):
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	lst=[];
	for data in devsvalue:
		if(checkOnIt(data.id,pmvalue,"showDevelopers")):
			lst.append(data)
	return render(request,"myAdmin/Another/showDevelopers.html",{"result":lst});

def showProManager(request):
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	lst=[];
	for data in pmvalue:
		lst.append(checkOnIt(int(data.DevsId),devsvalue,"showProManager"))
	return render(request,"myAdmin/Another/showProManager.html",{"result":lst});

def showHR(request):
	devsvalue=RecruitHr.objects.all();
	return render(request,"myAdmin/Another/showHR.html",{"result":devsvalue});



'''
def checkOnIt(SearchId,InSearch):
	for data in InSearch:
		if(SearchId==int(data.DevsId)):
			return data;
	else:
		return True;

def showDevelopers(request):
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	lst=[];
	for data in pmvalue:
		lst.append(data,checkOnIt(data.DevsId,devsvalue))
	return render(request,"myAdmin/Another/showDevelopers.html",{"result":lst});

def showProManager(request):
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	lst=[];
	for data in pmvalue:
		lst.append(data,checkOnIt(data.DevsId,devsvalue))
	return render(request,"myAdmin/Another/showDevelopers.html",{"result":lst});

'''









def RecruitDeveloperMethod(request):
	if request.method=="POST":
		values=RecruitDeveloper(FullName=request.POST["txtfname"],Age=request.POST["txtage"],MoblileNo=request.POST["txtmobileno"],EmailId=request.POST["txtemail"],WorkExperience=request.POST["txtworkexp"],Specialization=request.POST["txtprojectcategory"],Address=request.POST["txtaddress"],UserId=request.POST["txtuname"],Password=request.POST["txtpassword"])
		values.save()
		return render(request,"myAdmin/Collections/RecruitDeveloper.html",{"result":"_____'"+values.FullName+"' Registered, as Developer._____"})
	value=WorksOnLanguage.objects.all();
	return render(request,"myAdmin/Collections/RecruitDeveloper.html",{"values":value});





def RecruitHrMethod(request):
	if request.method=="POST":
		values=RecruitHr(FullName=request.POST["txtfname"],Age=request.POST["txtage"],MoblileNo=request.POST["txtmobileno"],EmailId=request.POST["txtemail"],WorkExperience=request.POST["txtworkexp"],Specialization=request.POST["txtprojectcategory"],Address=request.POST["txtaddress"],UserId=request.POST["txtuname"],Password=request.POST["txtpassword"])
		values.save()
		return render(request,"myAdmin/Collections/RecruitHr.html",{"result":"_____'"+values.FullName+"' Registered, as HR._____"})
	value=WorksOnLanguage.objects.all();
	return render(request,"myAdmin/Collections/RecruitHr.html",{"values":value});





def RecruitDeveloperAsProjectManagerMethod(request): 
	if request.method=="POST":
		myID=request.POST["txtdevelopercategory"]
		DevsData=RecruitDeveloper.objects.all();
		for data in DevsData:
			if(int(myID)==data.id):
				values=RecruitDeveloperAsProjectManager(FullName=data.FullName,UserId=data.UserId,DevsId=data.id)
				values.save()
				return render(request,"myAdmin/Collections/RecruitDeveloperAsProjectManager.html",{"result":"_____'"+values.FullName+"' promoted as proManager._____"});
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	lst=[];
	for data in devsvalue:
		if(checkOnIt(data.id,pmvalue,"showDevelopers")):
			lst.append(data)
	return render(request,"myAdmin/Collections/RecruitDeveloperAsProjectManager.html",{"values":lst});





def AddClientsAndProjectsByMyadminMethod(request): 
	if request.method=="POST":
		values=AddClientsAndProjectsByMyadmin(ClientsFullName=request.POST["txtfname"],ClientsEmailId=request.POST["txtemail"],ClientsMobileNo=request.POST["txtmobileno"],ProjectName=request.POST["txtpname"],ProjectLanguage=request.POST["txtprojectcategory"],ProjectStartDate=request.POST["txtsdate"],ProjectLastDate=request.POST["txtedate"],ProjectBudget=request.POST["txtbudget"],ClientsUserId=request.POST["txtuname"],ClientsPassword=request.POST["txtpassword"])
		values.save()
		return render(request,"myAdmin/Collections/AddClientsAndProjectsByMyadmin.html",{"result":"_____We added "+values.ClientsFullName+", as Client. And Its Project Name is '"+values.ProjectName+"'._____"});
	value=WorksOnLanguage.objects.all();
	return render(request,"myAdmin/Collections/AddClientsAndProjectsByMyadmin.html",{"values":value});





def FindData0(Search,inSearch,number):
	for data in inSearch:
		if(number==1 and Search==data.id):
			return data;
def AssignProjectToProjectManagerByMyadminMethod(request):
	if request.method=="POST":
		projectid=int(request.POST["txtprojectcategory"])
		pmid=int(request.POST["txtpmcategory"])
		projectvalue=AddClientsAndProjectsByMyadmin.objects.all();
		pmvalue=RecruitDeveloperAsProjectManager.objects.all();
		myData=[FindData0(projectid,projectvalue,1),FindData0(pmid,pmvalue,1)];
		values=AssignProjectToProjectManagerByMyadmin(ProManagerName=myData[1].FullName,ProjectName=myData[0].ProjectName,DevsId=myData[1].DevsId,ProManagerId=myData[1].id,ProjectId=myData[0].id)
		values.save()
		return render(request,"myAdmin/Collections/AssignProjectToProjectManagerByMyadmin.html",{"result":"_____We assigned project '"+myData[0].ProjectName+"', to project manager '"+myData[1].FullName+"'._____","more":[]});
	assignproject=AssignProjectToProjectManagerByMyadmin.objects.all();
	allprojects=AddClientsAndProjectsByMyadmin.objects.all();
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	projectvalue=[];
	for data in allprojects:
		if(checkOnIt(data.id,assignproject,"showDevelopers")):
			projectvalue.append(data)
	return render(request,"myAdmin/Collections/AssignProjectToProjectManagerByMyadmin.html",{"projectvalues":projectvalue,"pmvalues":pmvalue});












