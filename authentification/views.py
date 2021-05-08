from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login,authenticate,logout 
from django.contrib.auth.models import User
from django.contrib import messages
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
                    return redirect('home')
                else:
                    messages.error(request,"Désolé votre compte est désactivé")
                    return render(request,"login.html",{'formulaire':form}) 
            
            else:
                messages.error(request,"Identifiant ou mot de passe invalid")
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