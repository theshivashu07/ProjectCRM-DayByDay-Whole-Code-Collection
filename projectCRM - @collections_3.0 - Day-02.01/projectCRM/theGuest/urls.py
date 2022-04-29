from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('workprocess/',views.workprocess,name='workprocess'),
		path('aboutus/',views.aboutus,name='aboutus'),
		path('contactus/',views.contactus,name='contactus'),
		path('login/',views.login,name='login'),
		path('signup/',views.signup,name='signup'),
		#path('/',views.,name=''),
		
]


