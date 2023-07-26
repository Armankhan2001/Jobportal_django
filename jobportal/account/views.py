from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserPasswordResetSerializer,SendPasswordResetEmailSerializer, PersonalInfoSerializer, UserLoginSerializer,UserRegistrationSerializer,UserChangePasswordSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# from account.renderers import UserRenderer
# from django.dispatch import receiver
# from .models import User
# from django.core.signals import request_finished

# mysignal = Signal(providing_args = ['name'])

#Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegistrationView(APIView):
    # mysignal.send(sender = User, name = 'arman')
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg':'RegistrationSuccessful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response ({'token':token,'msg':'login Success'},status=status.HTTP_200_OK)
            else:
                return Response ({'errors': {'non_field_errors':['Email or Password is not Valid']}},status=status.HTTP_404_NOT_FOUND)
            

class UserProfileView(APIView):
    renderer_classes = [UserRenderer] 
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
       serializer = UserChangePasswordSerializer(data=request.data,
       context={'user':request.user})
       if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'},status=status.HTTP_200_OK)
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link send  Successfully, Please Check your Email..'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserPasswordResetView(APIView):
    renderer_classes  = [UserRenderer]
    def post(self, request, uid,token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data,context={'uid':uid, 'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PersonalInfo(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = PersonalInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Profile Created Successfully'},status=status.HTTP_200_OK)








# @receiver(request_finished)
# def func(sender, **kwargs):
#     print("Request Finished")
# @receiver(mysignal)
# def func2(sender, **kwargs):
#     print("\n\n", kwargs)