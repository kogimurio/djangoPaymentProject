from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<product_id>/', views.CheckOut, name='checkout'),
    path('payment-success/<int:product_id>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:product_id>/', views.paymentFailed, name='payment-failed'),
    path('pay/<id>/', views.pay, name='pay'),
]