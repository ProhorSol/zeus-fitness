from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('order/<int:subscription_id>/', views.order_subscription, name='order'),
    path('order/success/', views.order_success, name='order_success'),
]
