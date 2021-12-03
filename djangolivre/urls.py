from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from bank.urls import router

# API's endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]