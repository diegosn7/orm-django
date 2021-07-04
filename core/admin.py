from django.contrib import admin
from .models import Chassi, Carro, Montadora

# Register your models here.
@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    
    
@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora','modelo','chassi','preco')
    
@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)    

