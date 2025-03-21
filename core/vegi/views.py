from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.-----------------------------------------------------------
@login_required(login_url="/login/")
def receipes(request):

  if request.method =="POST":
    data = request.POST

    Receipe_image = request.FILES.get("Receipe_image")
    Receipe_name = data.get("Receipe_name")
    Receipe_description= data.get("Receipe_description")
  
    print(Receipe_name)
    print(Receipe_description)
    print(Receipe_image)  

    Receipe.objects.create (
      Receipe_image =Receipe_image,
      Receipe_name = Receipe_name,
      Receipe_description= Receipe_description
    )
    return redirect("/receipes/")
  
 
  setquery = Receipe.objects.all()
 
# this is for search receipe------------------------------------------------------------------------------------

  if request.GET.get('s-receipe'):
    setquery =setquery.filter(Receipe_name__icontains=request.GET.get('s-receipe'))
#----------------------------------------------------------------------------------------------------------------- 
 
  context ={"receipes": setquery}
  return render(request , 'receipes.html', context)



# this is for Update receipe------------------------------------------------------------------------------------
def update_receipe(request, id):
  
  setquery = Receipe.objects.get(id=id)
  if request.method =="POST":
    data = request.POST
    
  
    Receipe_name = data.get('Receipe_name') 
    Receipe_description= data.get('Receipe_description')
    Receipe_image = request.FILES.get('Receipe_image')

    setquery.Receipe_name = Receipe_name
    setquery.Receipe_description = Receipe_description
    

    if Receipe_image:
      setquery.Receipe_image = Receipe_image
    setquery.save()
    return redirect("/receipes/")

   
  return render(request , 'update_receipe.html', {"receipe": setquery})



# this is for delete receipe------------------------------------------------------------------------------------
def delete_receipe(request, id):
  Receipe.objects.all()
  setquery = Receipe.objects.get(id=id)
  setquery.delete()

  return redirect("/receipes/")


# this is for login user page --------------------------------------------------------------------------------------------
def login_user(request):
  if request.method =="POST":
    user_name = request.POST.get('username') 
    password = request.POST.get('password')

    if not User.objects.filter(username=user_name).exists():

       messages.warning(request, " User Does Not Exist ")
       return redirect("/login/")
    
    user = authenticate(username = user_name, password = password) # django inbuild method  

    if user is None:  
      messages.warning(request, " Invalid Credential ")
      return redirect("/login/")
    
    else:
      login(request ,user)
      return redirect("/receipes/")
    

  return render(request, "login.html")


 # this is for logout user page --------------------------------------------------------------------------------------------
def logout_page(request): 
  logout(request)
  return redirect("/login/")  

    
 
       

# this is for resister user page --------------------------------------------------------------------------------------------
def register_user(request):
   if request.method =="POST":

    first_name = request.POST.get('first_name') 
    last_name = request.POST.get('last_name') 
    user_name = request.POST.get('userid') 
    password = request.POST.get('password')

    if User.objects.filter(username=user_name).exists():
      messages.warning(request, "   User Name alredy Exist ")
      return redirect("/register/")
    else :
      messages.warning(request, "   Account resister succesfully  ")
      
    
    user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username =user_name

    )
    user.set_password(password)
    user.save()

     
   return render(request , 'register.html')