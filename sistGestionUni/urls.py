from django.contrib import admin
from django.urls import path
from academia.views import form_contacto, contactar

urlpatterns = [
    path('', admin.site.urls),
    path('form', form_contacto),
    path('contactar', contactar)
]
