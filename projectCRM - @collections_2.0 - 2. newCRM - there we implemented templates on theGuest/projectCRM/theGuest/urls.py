from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('aboutus/',views.aboutus,name='aboutus'),
		path('blogentries/',views.blogentries,name='blogentries'),
		path('contactus/',views.contactus,name='contactus'),
		path('pricingplans/',views.pricingplans,name='pricingplans'),
		path('testimonials/',views.testimonials,name='testimonials'),
		path('workprocess/',views.workprocess,name='workprocess'),
		#path('/',views.,name=''),
]


