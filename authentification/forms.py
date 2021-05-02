from django import forms
#Fromulaire de connexion
class LoginForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(attrs={'id':'identifiant','class':'form-control mb-2'}))
    password=forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'id':'password','class':'form-control mb-2'}))