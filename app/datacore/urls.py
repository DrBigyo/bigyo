from django.urls import include, path
from rest_framework import routers
from .views import ProductComparison

app_name = 'datacore'

urlpatterns = [
    path('some-path/', ProductComparison.as_view(), name='test'),
]
