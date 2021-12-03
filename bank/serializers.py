from rest_framework import serializers, fields
from .models import Clients, Account, Transfer


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = ('name', 
                  'cpf', 
                  'email', 
                  'birth_date', 
                  'address',  
                  'phone_number', 
                  'account', 
                  'created', 
                  'update', 
                  'active')
        # Can't POST without admin login
        # login = juntessomos | password = lgbtqiamais
        read_only_fields = ('cpf', )


class AccountSerializer(serializers.ModelSerializer):
    # Gets a dict with client's personal data
    clients = ClientSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('clients', 
                  'balance', 
                  'account_number', 
                  'agency', 
                  'created', 
                  'update')


class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = ('amount', 
                  'cpf_sender', 
                  'cpf_receiver', 
                  'created')


