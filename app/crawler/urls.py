from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crawler import views

urlpatterns = [
    path('snippets/', views.snippet_list),
]