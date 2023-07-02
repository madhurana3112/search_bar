from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication_api.serializers import CustomUserSerializer
from helper import *
from authentication_app.models import CustomUser
from django.contrib.auth import login, logout


class SignupAPI(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = generate_otp()
        user = CustomUser.objects.get(email=email)
        send_otp(user, otp)

        request.session['email'] = {
            'email': email,
            'otp': otp,
        }
        
        return Response({'message': 'OTP sent to email, please check'}, status=status.HTTP_200_OK)

class VerifyOTPAPI(APIView):
    def post(self, request):
        otp = int(request.data.get('otp'))
        email = request.data.get('email')
        email_session = request.session.get('email')
        
        if email_session['otp'] == otp and email_session['email'] == email:
            user = CustomUser.objects.get(email=email)
            login(request, user)
            return Response({'message': 'OTP verified'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
