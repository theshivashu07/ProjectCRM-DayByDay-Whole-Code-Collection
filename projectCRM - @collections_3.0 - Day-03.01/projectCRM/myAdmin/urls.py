from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('RecruitDeveloper/',views.RecruitDeveloperMethod,name='RecruitDeveloper'),
		path('RecruitHr/',views.RecruitHrMethod,name='RecruitHr'),
		path('RecruitDeveloperAsProjectManager/',views.RecruitDeveloperAsProjectManagerMethod,name='RecruitDeveloperAsProjectManager'),
		path('AddClientsAndProjectsByMyadmin/',views.AddClientsAndProjectsByMyadminMethod,name='AddClientsAndProjectsByMyadmin'),
		path('AssignProjectToProjectManagerByMyadmin/',views.AssignProjectToProjectManagerByMyadminMethod,name='AssignProjectToProjectManagerByMyadmin'),
		
		path('showDevelopers/',views.showDevelopers,name='showDevelopers'),
		path('showProManager/',views.showProManager,name='showProManager'),
		path('showHR/',views.showHR,name='showHR'),
		
		path('edits/',views.editsMethod,name='edits'),
		#path('editHR/',views.editHRMethod,name='editHR'),
		#path('editProjectManager/',views.editProjectManagerMethod,name='editProjectManager'),
		path('deletes/',views.deletes,name='deletes'),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		
		
]



