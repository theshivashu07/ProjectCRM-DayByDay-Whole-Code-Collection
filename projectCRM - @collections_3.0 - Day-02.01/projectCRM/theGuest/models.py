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
	Password = models.CharField(max_length=20);
	def __str__(self):
		return "We promote developer "+self.FullName+", as Project Manager.";



