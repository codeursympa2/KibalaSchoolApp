from django import forms
from django.contrib.auth.forms import PasswordChangeForm

#Fromulaire de connexion
class LoginForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur:",widget=forms.TextInput(attrs={'id':'identifiant','class':'mb-2 form-control','autofocus':''}))
    password=forms.CharField(label="Mot de passe:",widget=forms.PasswordInput(attrs={'id':'password','class':'mb-2 form-control'}))


#Formulaire du changement des infogrmation du compte

class AccountForm(forms.Form):
   
    last_password=forms.CharField(widget=forms.PasswordInput(attrs={'id':'last_password','class':'form-control mb-2'}),label="Mot de passe courant")
    password=forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','class':'form-control mb-2'}),label="Nouveau mot de passe")
    conf_password=forms.CharField(widget=forms.PasswordInput(attrs={'id':'conf_password','class':'form-control mb-2'}),label="Confirmer le mot de passe")
