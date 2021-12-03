from django.db import models
from django.core.validators import RegexValidator
from sequences import get_next_value

# Base Models from where other models will inherit attributs and methods
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Account's data model
class Account(Base):
    balance = models.FloatField()
    agency = models.CharField(max_length=10, default='0001')
    account_number = models.IntegerField(default=get_next_value('account', initial_value=10000), unique=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        unique_together = ['agency', 'account_number']

    def __str__(self) -> str:
        return str(getattr(self, 'id'))


# Client's personal data model
class Clients(Base):
    name = models.CharField(max_length=50, blank=False)
    cpf = models.CharField(max_length=11, 
                           unique=True, 
                           validators=[RegexValidator(regex='^.{11}$', 
                                       message='CPF inválido. Digite novamente.', 
                                       code='nomatch')], 
                                       blank=False)
    email = models.EmailField()
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11, 
                                    unique=True, 
                                    validators=[RegexValidator(regex='^.{11}$', 
                                    message='Número inválido. Digite novamente.', 
                                    code='nomatch')])
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'client'
        verbose_name = 'clients'
        
    def __str__(self) -> str:
        return self.name


# Transfer needed data model
# Gets 2 CPFs that will make the transactions
class Transfer(Base):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Valor') 
    cpf_sender = models.ForeignKey(Clients, 
                                   to_field="cpf", 
                                   on_delete=models.CASCADE, 
                                   related_name='transfer_sender', 
                                   verbose_name='Sender')
    cpf_receiver = models.ForeignKey(Clients, 
                                     to_field="cpf", 
                                     on_delete=models.CASCADE, 
                                     related_name='transfer_receiver', 
                                     verbose_name='Receiver')

    class Meta:
        verbose_name = 'transfer'
        verbose_name_plural = 'transfers'


    def str(self) -> str:
        return str(getattr(self, 'id'))
