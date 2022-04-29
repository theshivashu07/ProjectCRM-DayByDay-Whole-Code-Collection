from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('RecruitDeveloper/',views.RecruitDeveloperMethod,name='RecruitDeveloper'),
		path('RecruitHr/',views.RecruitHrMethod,name='RecruitHr'),
		path('RecruitDeveloperAsProjectManager/',views.RecruitDeveloperAsProjectManagerMethod,name='RecruitDeveloperAsProjectManager'),
		path('AddClientsAndProjectsByMyadmin/',views.AddClientsAndProjectsByMyadminMethod,name='AddClientsAndProjectsByMyadmin'),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		
		
]




