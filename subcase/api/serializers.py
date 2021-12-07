from django.utils import translation
from rest_framework import serializers
from subcase.models import Users, Organizations,Transactions







class OrganizationsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    org_name = serializers.CharField(max_length=200)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Organizations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.org_name = validated_data.get("org_name", instance.org_name)
        instance.save()
        return instance

class UsersSerializers(serializers.Serializer):
    #transactions = TransactionsSerializers(many=True)

    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(max_length=200)
    user_surname = serializers.CharField(max_length=200)
    user_balance = serializers.IntegerField()
    organizations = serializers.StringRelatedField(many=True, read_only=True)
    user_token = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get("user_name", instance.user_name)
        instance.user_surname = validated_data.get("user_surname", instance.user_surname)
        instance.user_balance = validated_data.get("user_balance", instance.user_balance)
        #instance.organizations = validated_data.get("organizations", instance.organizations)
        instance.user_token = validated_data.get("user_token", instance.user_token)

        instance.save()
        return instance


class TransactionsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    transaction_type = serializers.CharField(max_length=200)
    transaction_amount = serializers.IntegerField()
    transaction_status = serializers.CharField(max_length=200)
    #user_id = serializers.StringRelatedField()
    user_id = UsersSerializers()

    def create(self, validated_data):
        return Transactions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.transaction_type = validated_data.get("transaction_type", instance.transaction_type)
        instance.transaction_amount = validated_data.get("transaction_amount", instance.transaction_amount)
        instance.transaction_status = validated_data.get("transaction_status", instance.transaction_status)
        instance.save()
        return instance








