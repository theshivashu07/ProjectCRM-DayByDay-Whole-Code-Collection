from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('shortcodes/',views.shortcodesmethod,name='shortcodes'),
		path('simplepage/',views.simplepagemethod,name='simplepage'),
		#path('/',views.,name=''),
		
		
]




