from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import (generics, mixins, serializers, status,
                            viewsets)
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import Account, Clients, Transfer
from .serializers import (AccountSerializer, ClientSerializer,
                          TransferSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    # Athentication - only shows the content if logged in
    athentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # Athentication
    athentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Gets client's content
    @action(detail=True, methods=['get'])
    def clients(self, request, pk=None):
        account = self.get_object()
        serializer = ClientSerializer(account.clients.all())
        return Response(serializer.data)


class TransferViewSet(mixins.ListModelMixin, 
                      mixins.RetrieveModelMixin, 
                      viewsets.GenericViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # Athentication
    athentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # Allows search for some CPS's transfer history
    filter_backends = [SearchFilter]
    search_fields = ['cpf_sender__cpf', 'cpf_receiver__cpf']
    # Function to perform banking transactions
    # Returns a dict if the transaction when it occurs successfully
    # Retuns a error message if i does not.
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        sender = get_object_or_404(Clients, cpf=request.data['cpf_sender'])
        receiver = get_object_or_404(Clients, cpf=request.data['cpf_receiver'])
        account_sender = sender.account
        account_receiver = receiver.account
        amount = float(request.data['amount']) 
        if amount <= account_sender.balance and sender != receiver:
            account_sender.balance -= amount
            account_receiver.balance += amount
            account_sender.save()
            account_receiver.save()
            serializer.save()
            return Response({'transfer': {'amount': f'{amount:.2f}',   
                                          'from': f'{sender}', 
                                          'to': f'{receiver}'}
                                          }, 
                             status=status.HTTP_201_CREATED)
        return Response({'status': 'CPF inválido ou saldo insuficiente.'}, 
                         status=status.HTTP_400_BAD_REQUEST)
