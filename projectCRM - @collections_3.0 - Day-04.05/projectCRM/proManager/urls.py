from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		#path('ActiveAdmin/',views.ActiveAdminMethod,name='ActiveAdmin'),
		path('AssignProjectToDeveloperByProjectManager/',views.AssignProjectToDeveloperByProjectManagerMethod,name='AssignProjectToDeveloperByProjectManager'),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		
]




