from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import *
from . serializer import *

from rest_framework.views import APIView

from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework_simplejwt.tokens import RefreshToken

class registeruser(APIView):
    def post(self,request):
        data = request.data 
        serializer = userserializer(data = request.data)  
        if not serializer.is_valid():
            return Response({ 'status':403, 'error': serializer.errors ,'message': 'erorr'}) 
        serializer.save()
     #   user = User.objects.get(username = serializer.data['username'])
      #  token_obj = Token.objects.get_or_create(user = user) 
        refresh = RefreshToken.for_user(User)
        return Response({'status': 200, 'payload':serializer.data,
                            #'token': str(token_obj),
                            'message':' data saved',
                            'refresh': str(refresh),
                            'access': str(refresh.access_token)}) 








#APIView and api_view

@api_view(['GET'])
def get_student(request):
    student_objs = student.objects.all()  # get data 
    serializer = studentserializer(student_objs , many = True) # convert data into serialier
    return Response ({'status': 200, 'payload': serializer.data , 'message':' hello everyone'}) # sending serializer data


@api_view(['POST'])
def post_student(request):
   data = request.data 
   serializer = studentserializer(data = request.data)  
   if not serializer.is_valid():
       return Response({ 'status':403, 'error': serializer.errors ,'message': 'erorr'}) 
   serializer.save()
   return Response ({'status': 200, 'payload': serializer.data, 'message':' data saved'}) 


@api_view(['PUT'])
def put_student(request,id):
    try:
        student_obj = student.objects.get(id=id)
        serializer = studentserializer( student_obj, data = request.data)
        if not serializer.is_valid():
            return Response({ 'status':403, 'error': serializer.errors ,'message': 'erorr'}) 
        serializer.save()
        return Response ({'status': 200, 'payload': serializer.data, 'message':' data updated'})

    except Exception as e:
         return Response({ 'status':403,'message': ' invalid id'})
    


@api_view(['PATCH'])
def patch_student(request, id):
    try:
        student_obj = student.objects.get(id=id)
        serializer = studentserializer( student_obj, data = request.data , partial = True) # partial = true
        if not serializer.is_valid():
            return Response({ 'status':403, 'error': serializer.errors ,'message': 'erorr'}) 
        serializer.save()
        return Response ({'status': 200, 'payload': serializer.data, 'message':' data updated'})

    except Exception as e:
         return Response({ 'status':403,'message': ' invalid id'})
    


@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_obj = student.objects.get(id=id)
        student_obj.delete()
        return Response ({'status': 200, 'message':' data deleted'})
    except Exception as e:
         return Response({ 'status':403,'message': ' invalid id'})
    



# nested serializer book/category
@api_view(['GET'])
def get_book(request):
    book_objs = book.objects.all()
    serializer = bookserializer( book_objs, many = True)
    return Response({ 'status':200,'payload': serializer.data})
    

# apiview 

class studentapi(APIView):
    
   # authentication_classes = [TokenAuthentication] 
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]


    def get(self,request):
        student_objs = student.objects.all()  # get data 
        serializer = studentserializer(student_objs , many = True) # convert data into serialier
        return Response ({'status': 200, 'payload': serializer.data , 'message':' hello everyone'}) # sending serializer data
    
    def post(self , request):
         data = request.data 
         serializer = studentserializer(data = request.data)  
         if not serializer.is_valid():
             return Response({ 'status':403, 'error': serializer.errors ,'message': 'erorr'}) 
         serializer.save()
         return Response ({'status': 200, 'payload': serializer.data, 'message':' data saved'}) 
    
    def patch(self, request):
        try:
            student_obj = student.objects.get(id= request.data['id'])
            serializer = studentserializer( student_obj, data = request.data , partial = True) # partial = true
            if not serializer.is_valid():
                return Response({ 'status':403, 'error': serializer.errors ,'message': 'erorr'}) 
            serializer.save()
            return Response ({'status': 200, 'payload': serializer.data, 'message':' data updated'})

        except Exception as e:
             return Response({ 'status':403,'message': ' invalid id'})
        
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = student.objects.get(id=id)
            student_obj.delete()
            return Response ({'status': 200, 'message':' data deleted'})
        except Exception as e:
            return Response({ 'status':403,'message': ' invalid id'})
    


    



