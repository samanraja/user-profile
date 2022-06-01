from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, Hobbies, Address


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        user_obj = User.objects.create(**validated_data)
        profile_obj = UserProfile()
        profile_obj.user = user_obj
        profile_obj.save()
        return user_obj


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ('hobby_name',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'is_default',)
        read_only_fields = ('id', 'profile',)

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile

        address = Address.objects.create(**validated_data)
        address.profile = profile
        address.save()

        return address


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'profile_picture', 'hobbies', 'default_address',)
        read_only_fields = ('user',)

    def update(self, instance, validated_data):
        address = self.context['request'].data['default_address']
        address_id = address['id']
        address_name = address['address']
        is_default = address['is_default']

        address = Address.objects.get(id=address_id)
        address.is_default = is_default
        address.address = address_name
        address.save()

        return instance
