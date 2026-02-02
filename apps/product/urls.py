from django.urls import path
from rest_framework import urlpatterns

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailedAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('', views.ProductListCreateAPIView.as_view())
]