from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Tuteur(models.Model):
    Nom=models.CharField(max_length=20)
    Prenom=models.CharField(max_length=20)
    Sexe=models.CharField(max_length=20)
    StMat=models.CharField(max_length=20)
    
    def __str__(self):
        return ("Nom:{} | Prénom:{}").format(self.Nom,self.Prenom)
    
class Etudiant(models.Model):
    Matricle=models.CharField(primary_key=True,max_length=40,null=False)
    Nom=models.CharField(max_length=20)
    Prenom=models.CharField(max_length=20)
    DateNaiss=models.DateField(default=date.today)
    LieuNaiss=models.TextField(max_length=45)
    Sexe=models.CharField(max_length=20)
    Taille=models.FloatField()
    Photo=models.ImageField(null=True,blank=True)
    Nationalite=models.CharField(max_length=30)
    Tuteur=models.ForeignKey(Tuteur,on_delete=models.CASCADE)

    def __str__(self):
        return ("Nom:{} | Prénom:{} | Date de naissance: {}").format(self.Nom,self.Prenom,self.DateNaiss)


class Niveau(models.Model):
    Nom=models.CharField(max_length=15)
    
    def __str__(self):
        return (self.Nom)
    
class Paiement(models.Model):
    MontantMensuel=models.IntegerField()
    MontantInscription=models.IntegerField()
    Niveau=models.ForeignKey(Niveau,on_delete=models.CASCADE)
    
    def __str__(self):
        return ("Montant mensuel:{} | Niveau: {}").format(self.MontantMensuel,self.Niveau)

class Inscription(models.Model):
    DateInsc=models.DateTimeField(auto_now_add=True)
    Niveau=models.ForeignKey(Niveau,on_delete=models.CASCADE)
    Etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return ('Date d\'inscription:{} | par:{}').format(self.DateInsc,self.User)
