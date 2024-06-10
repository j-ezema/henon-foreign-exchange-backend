from django.urls import path
from .views import get_exchange_rates, retrieve_exchange_rates

urlpatterns = [
    path('exchange-rates/', get_exchange_rates, name='get_exchange_rates'),
    path('retrieve-rates/', retrieve_exchange_rates, name='retrieve_exchange_rates'),
]
 