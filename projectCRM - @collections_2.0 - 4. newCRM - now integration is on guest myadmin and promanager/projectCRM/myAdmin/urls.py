from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('blogentires/',views.blogentires,name='blogentires'),
		path('contactus/',views.contactus,name='contactus'),
		path('featured/',views.featured,name='featured'),
		path('presentation/',views.presentation,name='presentation'),
		path('recentwork/',views.recentwork,name='recentwork'),
		#path('/',views.,name=''),
		
		
]




