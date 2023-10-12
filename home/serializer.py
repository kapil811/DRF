
from rest_framework import serializers
from . models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        #fields = [ 'name', 'age']
        #exclude = ['id',]
        fields = '__all__'


    
    def validate(self , data):
        if data['age'] < 18:
             raise serializers.ValidationError({'error': " age cant be below 18"})
        

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': " name cant have integer"})
        
    
        return data
    



class categoryserializer( serializers.ModelSerializer):
    class Meta :
        model = category
        fields = "__all__"



class bookserializer(serializers.ModelSerializer):
    class Meta :
        category = categoryserializer()
        model = book
        fields = "__all__"




from django.contrib.auth.models import User

class userserializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
