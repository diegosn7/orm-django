from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField('Chassi',max_length=17, help_text='Informe até 17 caracteres.')
    
    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'
        
    def __str__(self):
        return self.numero
    
    
class Montadora(models.Model):
    nome = models.CharField('Nome',max_length=50, help_text='Até 50 caracteres.')
    
    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'
        
    def __str__(self):
        return self.nome
        
    
 #relação 1:1 entre carro e chassi - OneToOneField.
 #relação 1:* entre carro e montadora, uma montadora pode montar diversos carros.
 #relação *:* entre carro e motoristas, um motorista pode dirigir diversos carros e um carro pode ser dirigido por muitos motoristas    

class Carro(models.Model):
    chassi = models.OneToOneField(Chassi,on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo',max_length=30, help_text='Informe até 30 caracteres.')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        
    def __str__(self):
        return f'{self.montadora} {self.modelo}'