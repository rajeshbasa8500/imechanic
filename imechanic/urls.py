"""imechanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pip import main

from mainapp import views as mainapp_views
from adminapp import views as adminapp_views
from mechanicapp import views as mechanicapp_views
from userapp import views as userapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # main
    path('', mainapp_views.index, name='index'),
    path('about', mainapp_views.about, name='about'),
    path('contact', mainapp_views.contact, name='contact'),
    
    
    #admin
    path('admin-login',adminapp_views.admin_login,name='admin_login'),
    
    path('admin-logout',adminapp_views.admin_logout,name='admin_logout'),
    
    path('admin-add-authority',adminapp_views.admin_add_authority,name='admin_add_authority'),
    
    path('admin-manage-authority',adminapp_views.admin_manage_authority,name='admin_manage_authority'),
    
    path('admin-all-mechanic',adminapp_views.admin_all_mechanic,name='admin_all_mechanic'),
    
    path('admin-dashboard',adminapp_views.admin_dashboard,name='admin_dashboard'),
    
    path('admin_edit_authority/<int:id>/',adminapp_views.admin_edit_authority,name='admin_edit_authority'),
    
    path('admin-feedback-analysis',adminapp_views.admin_feedback_analysis,name='admin_feedback_analysis'),
    
    path('admin-manage-mechanic',adminapp_views.admin_manage_mechanic,name='admin_manage_mechanic'),
    
    path('admin-pending-mechanic',adminapp_views.admin_pending_mechanic,name='admin_pending_mechanic'),
    
    path('admin-sentement-analysis-graph',adminapp_views.admin_sentement_analysis_graph,name='admin_sentement_analysis_graph'),
    
    path('admin-user-details',adminapp_views.admin_user_details,name='admin_user_details'),
    
    path('update/<int:id>',adminapp_views.update,name='update'),
    
    path('reject/<int:id>',adminapp_views.reject,name='reject'),
    
    path('manage/<int:id>',adminapp_views.manage,name='manage'),
    
    
    
    #mechanic
    
    path('mechanic-login',mechanicapp_views.mechanic_login,name='mechanic_login'),
    
    path('mechanic-logout',mechanicapp_views.mechanic_logout,name='mechanic_logout'),
    
    path('mechanic-add-shop',mechanicapp_views.mechanic_add_shop,name='mechanic_add_shop'),
    
    path('mechanic-manage-shop',mechanicapp_views.mechanic_manage_shop,name='mechanic_manage_shop'),
    
    path('mechanic-confirmed-booking',mechanicapp_views.mechanic_confirmed_booking,name='mechanic_confirmed_booking'),
    
    path('mechanic-dashboard',mechanicapp_views.mechanic_dashboard,name='mechanic_dashboard'),
    
    path('mechanic_edit_shop/<int:id>/',mechanicapp_views.mechanic_edit_shop,name='mechanic_edit_shop'),
    
    path('mechanic-my-feedback',mechanicapp_views.mechanic_my_feedback,name='mechanic_my_feedback'),
    
    path('mechanic-pending-booking',mechanicapp_views.mechanic_pending_booking,name='mechanic_pending_booking'),
       
    path('mechanic-register',mechanicapp_views.mechanic_register,name='mechanic_register'),
    
    path('map/<int:id>/',mechanicapp_views.map,name='map'),
    
    path('accept/<int:book_id>/',mechanicapp_views.accept,name='accept'),
    
    # path('search',mechanicapp_views.search,name='search'),
    
    #user
    
    path('user-book-appointment',userapp_views.user_book_appointment,name='user_book_appointment'),
    
    path('user-dashboard',userapp_views.user_dashboard,name='user_dashboard'),
    
    path('user_feedback/<int:id>/<int:mechanic>/',userapp_views.user_feedback,name='user_feedback'),
    
    path('user-my-booking',userapp_views.user_my_booking,name='user_my_booking'),
    
    path('user-myprofile',userapp_views.user_myprofile,name='user_myprofile'),
    
    path('user-registration',userapp_views.user_registration,name='user_registration'),
    
    path('user-services',userapp_views.user_services,name='user_services'),
    
    path('user-login',userapp_views.user_login,name='user_login'),
    
    path('user-map',userapp_views.user_map,name='user_map'),
    
    path('user-book-mechanic',userapp_views.user_book_mechanic,name='user_book_mechanic'),
    
    path('user_mechanic_appoinment/<int:id>/',userapp_views.user_mechanic_appoinement,name='user_mechanic_appoinement')
    
  
    
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

