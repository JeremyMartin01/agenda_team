from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        #exclude = ('created', 'modified')
        fields = ('__all__')        

#NO ESTA VINCULADO AL MODELO PERSON
class PersonaSerializer(serializers.Serializer):    
    id = serializers.IntegerField() #En modelo el ID siempre es Entero
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    
    #No es frecuente, pero veces se requiere agregar atributos extras, al serializer
    #activo = serializers.BooleanField(default=False)#No pertenece al modelo persona
    activo = serializers.BooleanField(required=False)#No pertenece al modelo persona

class PersonaSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(required=False)#Campo no perteneciente al modelo Persona
    '''Importante: Se puede agregar campos que no pertenecen al modelo, de preferencia que sean datos fijos,
    osea que no sean dinámico para cada registro, por ejemplo si el campo activo cambiara (True o False) para 
    cada persona, entonces será necesario definirlo en el modelo'''
    class Meta:
        model = Person
        fields = ('__all__') # Incluir todos los campos del modelo Persona en la representación JSON

    '''def to_representation(self, instance):               
        representation = super().to_representation(instance)
        representation['activo'] = self.context['request'].query_params.get('activo', True)
        representation['hobbies']= []
        for hobby in instance.hobbies.all():
            representation['hobbies'].append(hobby.hobby)
        return representation'''
    
    # el mismo código de arriba pero optimizado.
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['activo'] = self.context['request'].query_params.get('activo', True)
        representation['hobbies'] = [hobby.hobby for hobby in instance.hobbies.all()]
        return representation
        
class ReunionSerializer(serializers.ModelSerializer):
    persona = PersonSerializer()
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha', 
            'hora', 
            'asunto',
            'persona'
        )

class Hobbyserializers(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')

class PersonaSerializer3(serializers.ModelSerializer):
      hobbies = Hobbyserializers(many=True)# many=True que serializer este seriador, pero que tenga en cuenta que tambien seria una colección.
      class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created'
        )
       
class ReunionSerializer2(serializers.ModelSerializer):   
    
    fecha_hora = serializers.SerializerMethodField()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha', 
            'hora', 
            'asunto',
            'persona',
            'fecha_hora'#Es importante agregarlo ahi, 
        )    
    #Combinacion de fecha y hora,  que no existe en el modelo
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' _ ' + str(obj.hora)

class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):   
        
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha', 
            'hora', 
            'asunto',
            'persona'   
        ) 
        extra_kwargs = {
            'persona': {'view_name':'persona_app:detalle', 'lookup_field':'pk'}
        }

class PersonPagination(pagination.PageNumberPagination):
    page_size = 5 #Bloque de 5
    max_page_size = 100 #Tamaño maximo que cargue en memoria

class CountReunionSerializer(serializers.Serializer):    
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()