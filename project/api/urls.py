from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView, CategoryAPIView, ManufacturerAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('manufacturers/', ManufacturerAPIView.as_view()),
]