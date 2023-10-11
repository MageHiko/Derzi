from account.models import Account
from rest_framework import serializers

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ('password')
    
class AccountCreateSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password')

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"