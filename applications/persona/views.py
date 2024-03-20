from django.shortcuts import render
from django.views.generic import ListView, TemplateView
#
from rest_framework.generics import (
    ListAPIView,#Listar
    CreateAPIView,#Crear
    RetrieveAPIView,#Detalle de persona
    DestroyAPIView,#Eliminar
    UpdateAPIView ,#Modificar 
    RetrieveUpdateAPIView #Modificar pero trae los datos en el formulario
    )

from .models import Person, Reunion, Hobby
from .serializer import (
    PersonSerializer, 
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer
)

class ListaPersonas(ListView):
    #model = Person
    template_name = "persona/personas.html"
    context_object_name = 'personas' #enviando al HTML para que haga una operación
    
    def get_queryset(self):
        return Person.objects.all()

'''VISTAS GENÉRICAS DJANGO'''
#LISTADO
class PersonListApiView(ListAPIView):
    #Serializer
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = 'persona/lista.html'

#LISTADO
class PersonSearchApiView(ListAPIView):
   serializer_class = PersonSerializer
   
   def get_queryset(self):
       #filtramos datos
       kword  = self.kwargs['kword'] #recuperamos un dato
       return Person.objects.filter(
           full_name__icontains = kword
       )

#CREACIÓN
class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer

#VER DETALLES
class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()#conjunto de datos donde se hara la busqueda del registro

#ELIMINAR
class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#ACTUALIZAR TODOS LOS DATOS SIN RECUPERAR NADA DEL UPDATE   
class PersonUpdateView(UpdateAPIView):    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#RECUPERA DATOS (se visualiza en los forms) y ACTUALIZA
class PersonRetrieveUpdateView(RetrieveUpdateAPIView):    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#LISTADO   
class PersonApiLista(ListAPIView):
    """     
    Vista para interactuar con serializadores    
    """
    """    
    Cuando nosotros intentemos serializar algo siempre el serializador va a recibir un query set  
    """
    #serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer2
    #serializer_class = PersonaSerializer3
    def get_queryset(self):
        return  Person.objects.all()

#LISTADO
class ReunionSerializer2(ListAPIView):    
    serializer_class = ReunionSerializer
    def get_queryset(self):
        return  Reunion.objects.all()

#LISTADO
class ReunionApiListLink(ListAPIView):  
      
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
        return  Reunion.objects.all()

#LISTADO
class PersonPaginationList(ListAPIView):  
    '''
    Lista personas con paginacion    
    '''      
    serializer_class = PersonaSerializer    
    pagination_class = PersonPagination
    
    def get_queryset(self):
        return  Person.objects.all()

#LISTADO
class ReunioByPersonJob(ListAPIView):  
    serializer_class = CountReunionSerializer
    
    def get_queryset(self):
        return  Reunion.objects.cantidad_reuniones_job()