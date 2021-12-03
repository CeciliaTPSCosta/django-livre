from django.contrib import admin

from .models import Account, Clients, Transfer


admin.site.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 
                    'cpf', 
                    'email', 
                    'birth_date', 
                    'adress', 
                    'phone_number', 
                    'account', 
                    'publicacao', 
                    'atualizacao', 
                    'ativo']


admin.site.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['balance', 
                    'agency', 
                    'account_number', 
                    'publicacao', 
                    'atualizacao', 
                    'ativo']


admin.site.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['amount', 
                    'cpf_sender', 
                    'cpf_receiver', 
                    'publicacao', 
                    'atualizacao', 
                    'ativo']

