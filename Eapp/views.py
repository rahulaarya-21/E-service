from django.shortcuts import *
from .models import *
# Create your views here.
def register2(request):
    return render(request,"Eapp/register2.html")

def indexpage(request):
    return render(request,"Eapp/index.html")

def servicepage(request):
    return render(request,"Eapp/services.html")

def projectpage(request):
    return render(request,"Eapp/projects.html")

def contactpage(request):
    return render(request,"Eapp/contact.html")

def aboutpage(request):
    return render(request,"Eapp/about.html")

def statuspage(request):
    return render(request,"Eapp/status.html")
    
def loginpage(request):
    return render(request,"Eapp/login.html")

def doctordash(request):
    return render(request,"Eapp/login.html")



def rig(request):
        if request.POST['role'] =='ServiceMan':
                role=request.POST['role']
                name=request.POST['firstname']
                email=request.POST['email']
                phone=str(request.POST['num'])
                address=request.POST['add']
                password=request.POST['password']

                user=User.objects.filter(user_email=email)
                if user:
                        message='This email already exists'
                        return render(request,"Eapp/register2.html",{'message':message})
                else:
                        newuser=User.objects.create(user_email=email,user_password=password,user_role=role)
                        servicemenuser=Servicemen.objects.create(userid=newuser,servicemen_name=name,servicemen_phone=phone,servicemen_address=address)
                        return render(request,"Eapp/login.html")

        if request.POST['role'] =='Customer':
                role=request.POST['role']
                name=request.POST['firstname']
                email=request.POST['email']
                phone=str(request.POST['num'])
                address=request.POST['add']
                password=request.POST['password']

                user=User.objects.filter(user_email=email)
                if user:
                        message='This email already exists'
                        return render(request,"Eapp/register2.html",{'message':message})

                else:
                        newuser=User.objects.create(user_email=email,user_password=password,user_role=role)
                        Customeruser=Customer.objects.create(userid=newuser,customer_name=name,customer_phone=phone,customer_address=address)
                        return render(request,"Eapp/login.html")



def loginevaluate(request):
        if(request.POST['role']=='ServiceMan'):
                email=request.POST['email']
                password=request.POST['password']
                user=User.objects.filter(user_email=email)
                
                if(user[0]):
                        if(user[0].user_password==password and user[0].user_role == 'ServiceMan'):
                                servicemen=Servicemen.objects.filter(userid=user[0].id)
                                request.session['email']=user[0].user_email
                                #request.session['name']=user[0].ServiceMan_name
                                request.session['role']=user[0].user_role
                                #request.session['id']=user[0].userid
                                return HttpResponseRedirect(reverse('header'))
                        else:
                                message = "Your password is incorrect or user doesn't exist"
                                return render(request, "Eapp/login.html", {'message': message})

                else:
                        message:"user doesn't exist"
                        return render(request, "Eapp/login.html", {'message': message})
        elif(request.POST['role']=='Customer'):
                email=request.POST['email']
                password=request.POST['password']
                user=User.objects.filter(user_email=email)
                if(user[0]):
                        if(user[0].user_password==password and user[0].user_role== 'Customer'):
                                servicemen=Servicemen.objects.filter(userid=user[0])
                                request.session['email']=user[0].user_email
                                #request.session['name']=user[0].Customer_name
                                request.session['role']=user[0].user_role
                                #request.session['id']=user[0].userid
                                return HttpResponseRedirect(reverse('header'))
                        else:
                                message = "Your password is incorrect or user doesn't exist"
                                return render(request, "Eapp/login.html", {'message': message})

                else:
                        message:"user doesn't exist"
                        return render(request, "Eapp/login.html", {'message': message})
        else:
                message="Login Failed"
                return render(request,"Eapp/login.html",{'message':message})

def HeaderPage(request):
        if(("email" in request.session) and ("role" in request.session)):
                if request.session['role']=="ServiceMan":
                        all_serviceman = Servicemen.objects.all()
                        return render(request,"Eapp/sucess.html",{"allserviceman":all_serviceman})
                else:
                        all_customer = Customer.objects.all()
                        return render(request,"Eapp/sucess.html",{"allcustomer":all_customer})
        else:
                return HttpResponseRedirect(reverse("Login"))
