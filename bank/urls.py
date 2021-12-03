from django.db import router
from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .views import ClientViewSet, AccountViewSet, TransferViewSet

# API's routes
router = SimpleRouter()
router.register('clients', ClientViewSet)
router.register('accounts', AccountViewSet)
router.register('transfers', TransferViewSet)