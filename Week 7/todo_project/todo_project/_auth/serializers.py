from rest_framework import serializers
from todo_project._auth.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'is_superuser', 'password',)

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
