from django_rest_passwordreset.views import ResetPasswordRequestToken,ResetPasswordConfirm
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from account.serializers import UserSerializer,EmailSerializer,ResetPasswordSerializer

class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.data,status = status.HTTP_201_CREATED)


class EmailVerification(APIView):
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):
        serializer = EmailSerializer(data = request.data)
        if serializer.is_valid():
            serialized_user = serializer.validated_data.get('email')
            email = serialized_user
            user = User.objects.get(email=email)
            tok = PasswordResetTokenGenerator().make_token(user)
            send_mail(
                "reset password",
                "reset the password using given token {}".format(tok),
                f"{settings.EMAIL_HOST_USER}",
                [f"{serialized_user}"],
                fail_silently = False,
            )
            context = {
                'user':serialized_user,
                'message':'mail sent'
            }
            return Response(context)
        return Response(serializer.errors)


class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request,*args,**kwargs):
        serializer = ResetPasswordSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            toke = serializer.validated_data.get('token')
            user = User.objects.get(email = email)
            token = PasswordResetTokenGenerator().check_token(user,toke)
            if token:
                user.set_password(serializer.validated_data.get('password'))
                user.save()
                print('saved')
            return Response(serializer.data)
        return Response(serializer.errors)
