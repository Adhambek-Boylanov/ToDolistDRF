from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self,attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"User does not exist"
                }
            )
        auth_user = authenticate(username = user.username,password = password)
        if auth_user is None:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"Username or password is invalid"
                }
            )
        attrs["user"] = auth_user
        return attrs
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"