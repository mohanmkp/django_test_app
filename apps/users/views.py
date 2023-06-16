import traceback

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.users.serializers import signup
from apps.users.serializers import login
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework import status




def sending_mail(otp, mail):
    try:
        subject = "Visiontrek Card"
        text_content = 'Verify your email address'
        html_content = render_to_string('email.html', {
            'otp': otp
        })
        send_mail(subject, text_content, 'mohan.pandit@visiontrek.in', [mail],  html_message=html_content,)
    except Exception as e:
        print(e)
        traceback.print_exc()
        print("mail not send")



class UserAction(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = signup.Sign_Up_Serializer

    def post(self, request, *args, **kwargs):
        serializer = signup.Sign_Up_Serializer(data=request.data)
        sending_mail(otp="454544", mail="prajapatimohan241@gmail.com")

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(user.password)
            user.email = user.email.lower()
            user.is_active = True
            user.save()
            token = Token.objects.create(user=user)
            return Response({
                "msg": "signup successfully",
                "token": token.key
            })



class SingIn(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = login.SignInSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            UserModel = get_user_model()
            try:
                user = User.objects.get(email=serializer.data['email'])
            except UserModel.DoesNotExist:
                return Response({
                    "msg": "invalid email",
                }, status=status.HTTP_404_NOT_FOUND)
            else:
                password = serializer.data['password']
                if user.check_password(password):
                    token, created = Token.objects.get_or_create(user=user)
                    print(token)
                    return Response({
                        "msg": "signin successfully",
                        "token": token.key,
                        "first_name": user.first_name,
                        "usr_id": user.id
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "msg": "invalid password",
                    }, status=status.HTTP_401_UNAUTHORIZED)










