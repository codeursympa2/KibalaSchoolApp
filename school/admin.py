from django.contrib import admin

# Register your models here.
from .models import *
 
admin.site.register(Etudiant)
admin.site.register(Paiement)
admin.site.register(Niveau)
admin.site.register(Inscription)
admin.site.register(Tuteur)
 
 
