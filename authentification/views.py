from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate,logout 
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_blog(request):
    
    if request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            #
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #
            user=authenticate(username=username,password=password)
            #
            if user is not None:
                if user.is_active:
                    login(request,user)
                    messages.success(request,"Connexion reussie")
                    return redirect('home')
                else:
                    messages.error(request,"Désolé votre compte est désactivé")
                    return render(request,"login.html",{'formulaire':form}) 
            
            else:
                messages.error(request,"Identifiant ou mot de passe invalide")
                return render(request,"login.html",{'formulaire':form})        
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] +=' is-invalid'
            return render(request,"login.html",{'formulaire':form})
    #
    form=LoginForm()
    return render(request,"login.html",{'formulaire':form})

def logout_view(request):
    logout(request)
    return redirect('connexion')

@login_required
def change_view(request):
    form=PasswordChangeForm(data=request.POST,user=request.user)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.info(request,"Connectez vous avec votre nouveau mot de passe.")
            return redirect('/')  
        else:
            messages.error(request,"Veillez saisir des informations correctes")
            return render(request,'account.html',{'form':form})
    return render(request,'account.html',{'form':form})