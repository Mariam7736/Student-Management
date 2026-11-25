from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from StudentApp.models import Student
from StudentApp.serializers import RegistrationSerializer,StudentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.
class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer_instance=RegistrationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "message":"REGISTRATION SUCCESSFULL"
            })
        else:
            return Response(serializer_instance.errors)

class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"message": "Invalid username or password"})




        
    
    

        

class StudentListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        students=Student.objects.all()
        serializer_instance=StudentSerializer(students,many=True)
        return Response(serializer_instance.data)
