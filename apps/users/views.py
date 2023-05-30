from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.users.serializers import signup
from apps.users.serializers import login
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework import status



class UserAction(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = signup.Sign_Up_Serializer

    def post(self, request, *args, **kwargs):
        serializer = signup.Sign_Up_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(user.password)
            user.email = user.email.lower()
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
                    token = Token.objects.get(user=user)
                    return Response({
                        "msg": "signin successfully",
                        "token": token.key,
                        "first_name": user.first_name,
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "msg": "invalid password",
                    }, status=status.HTTP_401_UNAUTHORIZED)










