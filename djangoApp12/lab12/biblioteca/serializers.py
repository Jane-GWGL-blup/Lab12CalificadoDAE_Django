from rest_framework import serializers 

from .models import Prestamos

class PrestamosSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    idLibro = serializers.IntegerField()
    idUsuario = serializers.IntegerField()
    fecPrestamo= serializers.DateField()
    fecDevolucion= serializers.DateField()

    class Meta: 
        model = Prestamos 
        fields = ('id', 'idLibro', 'idUsuario', 'fecPrestamo', 'fecDevolucion')

    def create(self, validated_data): 
        """ 
        Create and return a new `Prestamos` instance, given the validated data. 
        """ 
        return Prestamos.objects.create(**validated_data) 

    def update(self, instance, validated_data): 
        """ 
        Update and return an existing `Prestamos` instance, given the validated data. 
        """ 
        instance.idLibro = validated_data.get('idLibro', instance.idLibro) 
        instance.idUsuario = validated_data.get('idUsuario', instance.idUsuario) 
        instance.fecPrestamos = validated_data.get('fecPrestamo', instance.fecPrestamo) 
        instance.fecDevolucion = validated_data.get('fecDevolucion', instance.fecDevolucion) 
        instance.save() 
        return instance 
    
class PrestamosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Prestamos 
        fields = ('id', 'idLibro', 'idUsuario', 'fecPrestamo', 'fecDevolucion')