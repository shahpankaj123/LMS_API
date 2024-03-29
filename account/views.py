from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import UserRegisterSerializer,UserLoginSerializer,ProfileSerializer,UserchangepasswordSerializer,UserSendMailSerializer,UserPasswordResetSerializer,UserProfileViewSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegisterView(APIView):
    def post(self,request,format=None):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration successfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login successfull'},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'msg':'Login unsuccessfull'},status=status.HTTP_404_NOT_FOUND)
        return Response({'msg':'erroe'},status=status.HTTP_400_BAD_REQUEST)    


class Profileview(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=ProfileSerializer(request.user) 
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserchangepasswordView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer= UserchangepasswordSerializer(data=request.data,context={'user':request.user}) 
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserSendMailView(APIView):
    def post(self,request,format=None):
        serializer=UserSendMailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Email Send Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    def post(self,request,uid,token,format=None):
        serializer=UserPasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class All_UserProfileView(APIView): 
    def get(self,request,format=None):
        user=User.objects.all()
        print(user)
        serializer=UserProfileViewSerializer(user,many=True) 
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserProfile_ByIDView(APIView): 
    def get(self,request,id,format=None):
        user=get_object_or_404(User,id=id)
        print(user)
        if user:
          serializer=UserProfileViewSerializer(user) 
          return Response(serializer.data,status=status.HTTP_200_OK)            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

