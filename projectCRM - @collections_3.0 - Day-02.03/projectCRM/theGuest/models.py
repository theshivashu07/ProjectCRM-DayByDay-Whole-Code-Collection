from django.db import models





class WorksOnLanguage(models.Model):
	Language = models.CharField(max_length=30);
	def __str__(self):
		return "We Added new Language "+self.Language+".";


class RecruitDeveloper(models.Model): 
	FullName = models.CharField(max_length=20);
	Age = models.CharField(max_length=2);
	MoblileNo = models.CharField(max_length=10);
	EmailId = models.CharField(max_length=30);
	WorkExperience = models.CharField(max_length=2);
	Specialization = models.CharField(max_length=25);
	Address = models.CharField(max_length=50);
	UserId = models.CharField(max_length=25);
	Password = models.CharField(max_length=25);
	def __str__(self):
		return "We hiring "+self.FullName+", as Developer.";


class RecruitHr(models.Model): 
	FullName = models.CharField(max_length=20);
	Age = models.CharField(max_length=2);
	MoblileNo = models.CharField(max_length=10);
	EmailId = models.CharField(max_length=30);
	WorkExperience = models.CharField(max_length=2);
	Specialization = models.CharField(max_length=25);
	Address = models.CharField(max_length=50);
	UserId = models.CharField(max_length=25);
	Password = models.CharField(max_length=25);
	def __str__(self):
		return "We hiring "+self.FullName+", as HR.";


class RecruitDeveloperAsProjectManager(models.Model): 
	FullName = models.CharField(max_length=20);
	UserId = models.CharField(max_length=20);
	DevsId = models.CharField(max_length=10); 
	def __str__(self):
		return "We promote developer "+self.FullName+", as Project Manager.";


class AddClientsAndProjectsByMyadmin(models.Model):
	ClientsFullName = models.CharField(max_length=20);
	ClientsEmailId = models.CharField(max_length=30);
	ClientsMobileNo = models.CharField(max_length=10);
	ProjectName = models.CharField(max_length=30);
	ProjectLanguage = models.CharField(max_length=30);
	ProjectStartDate = models.CharField(max_length=10);
	ProjectLastDate = models.CharField(max_length=10);
	ProjectBudget = models.CharField(max_length=6);
	ClientsUserId = models.CharField(max_length=25);
	ClientsPassword = models.CharField(max_length=25);
	def __str__(self):
		return "We added "+self.ClientsFullName+", as Client. And Its Project Name is '"+self.ProjectName+"'.";


class AssignProjectToProjectManagerByMyadmin(models.Model):
	ProManagerName = models.CharField(max_length=20); 
	ProjectName = models.CharField(max_length=30);
	DevsId = models.CharField(max_length=10);
	ProManagerId = models.CharField(max_length=10); 
	ProjectId = models.CharField(max_length=10); 
	def __str__(self):
		return "We assigned project '"+self.ProjectName+"', to project manager '"+self.ProManagerName+"'.";










'''


class ProjectReport(models.Model):
	ProjectName= models.CharField(max_length=30); 
	ProjectId= models.CharField(max_length=10); 
	DevsId= models.CharField(max_length=10); 
	ProManagerId= models.CharField(max_length=10); 
	ProjectStatus= models.CharField(max_length=20);
	ProjectDescription= models.CharField(max_length=50);
	ReportTo=models.CharField(max_length=20); 
	Status= models.CharField(max_length=20); 
	def __str__(self): 
		return "This "+self.ProjectName+"'s project Report to "+self.ReportTo+"."; 






class AssignProjectToDeveloperByProjectManager(modules.Model):
	DeveloperName=
	ProjectName = models.CharField(max_length=30);
	ProManagerId = models.CharField(max_length=10);
	ProjectId = models.CharField(max_length=10);
	DevsId = models.CharField(max_length=10);

'''