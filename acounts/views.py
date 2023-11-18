from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()


def login_user(request):
    if request.method == 'POST':
        #traiter le formulaire connecter l'utilisateur
       username = request.POST.get("username")#pour recuperer les donnees du formulaire du champ name de l'input username 
       password = request.POST.get("password")#pour recuperer les donnees du formulaire du champ name de l'input password  
       user = authenticate(username=username, password=password)
       if user: #si l'utilisateur existe
           login(request, user)
           return render(request, 'base.html')
    return render(request, 'accounts/login.html')

def page_login(request):
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
