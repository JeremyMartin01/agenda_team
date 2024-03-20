#
from model_utils.models import TimeStampedModel
#
from django.db import models
from .manager import ReunionManager

#TimeStampedModel traer instalado el models util
#Dentro de nuestra agenda vamos a guardar los pasatiempos de cada persona que estemos registrando.
class Hobby(TimeStampedModel):
    '''Pasa Tiempos'''
    hobby = models.CharField(
        'Pasa tiempo',
        max_length=50,
    )    
    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
    def __str__(self):
        return self.hobby

#
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    #Relacion de muchos a muchos con la tabla Hobby
    hobbies = models.ManyToManyField(
        Hobby
    )
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name +" | "+ self.job 
    
#***********************************************************
class Reunion(TimeStampedModel):
    """Modelo para reunión"""
    persona = models.ForeignKey( #ForeignKey hacia la tabla persona
        Person,
        on_delete = models.CASCADE
    )
    fecha = models.DateField()#Fecha de reuniones que tenemos con las personas
    hora = models.TimeField()
    asunto = models.CharField(
            'Asunto de Reunión',
             max_length = 100
    )
    objects = ReunionManager()
    class Meta:
        verbose_name = 'Reunión'
        verbose_name_plural = 'Reunión'
        
    def __str__(self):
        return self.asunto + " | " + self.persona.full_name
    
