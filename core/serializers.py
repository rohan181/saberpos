from rest_framework import serializers
from .models import UserItem, Product

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    product = ProductInfoSerializer()  
    #name1= serializers.SlugRelatedField(many=True, read_only=True,slug_field='name')
    

    class Meta:
        model = UserItem
        fields ='__all__'
        

	    