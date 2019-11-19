from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.indexpage,name="Indexpage"),

    path("services/",views.servicepage,name="Service"),
    path("projects/",views.projectpage,name="Project"),
    path("Contacts/",views.contactpage,name="Contact"),
    path("Aboutus/",views.aboutpage,name="Aboutus"),
    path("Track/",views.statuspage,name="Status"),
    path("logindata",views.loginevaluate,name="logindata"),
    path("login/",views.loginpage,name="Login"),
    path("login1/",views.HeaderPage,name="header"),
    path("rig",views.rig,name="rig"),
    path("register2/",views.register2,name="register2"),
    path("doctorDashbord",views.doctordash,name="doctorDashbord")

    
]


