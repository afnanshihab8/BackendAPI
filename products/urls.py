from django.urls import path
from .views import ProductListCreate, ProductDetail, CommentCreate, RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register"),
    path('products/', ProductListCreate.as_view(), name="product-list"),
    path('products/<int:pk>/', ProductDetail.as_view(), name="product-detail"),
    path('products/<int:product_id>/comments/', CommentCreate.as_view(), name="add-comment"),
]
