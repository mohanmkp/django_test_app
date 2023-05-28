from .comman import *

class Sign_Up_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "gender",
            "mobile_number",
            "profile_pic"
        ]

