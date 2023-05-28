from .comman import *


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    class Meta:
        fields = ["email", "password"]




