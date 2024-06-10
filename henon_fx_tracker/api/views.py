from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import CADExchangeRate, EURExchangeRate, USDExchangeRate
import logging
from decimal import Decimal, InvalidOperation
import requests 

logger = logging.getLogger(__name__)

def retrieve_exchange_rates(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    base_currency = request.GET.get('base_currency')

    if not all([start_date_str, end_date_str, base_currency]):
        logger.error(f"Missing parameters: start_date={start_date_str}, end_date={end_date_str}, base_currency={base_currency}")
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    try:
        start_date = datetime.strptime(start_date_str, '%B %d, %Y').date()
        end_date = datetime.strptime(end_date_str, '%B %d, %Y').date()
    except ValueError as e:
        return JsonResponse({'error': f'Invalid date format: {e}'}, status=400)

    model_mapping = {
        'CAD': CADExchangeRate,
        'EUR': EURExchangeRate,
        'USD': USDExchangeRate,
    }

    model = model_mapping.get(base_currency)
    if not model:
        logger.error(f"Invalid base currency: {base_currency}")
        return JsonResponse({'error': 'Invalid base currency'}, status=400)

    rates = model.objects.filter(date__range=[start_date, end_date]).order_by('-date')
    
    if not rates.exists():
        latest_rate = model.objects.latest('date')
        rates = model.objects.filter(date=latest_rate.date)

    if not rates:
        return JsonResponse({'error': 'No data available'}, status=404)

    exchange_data = {base_currency: []}

    for rate in rates:
        exchange_data[base_currency].append({'currency': rate.currency, 'date': rate.date, 'rate': rate.rate})

    return JsonResponse(exchange_data)

def get_exchange_rates(request):
    base_url = "https://api.frankfurter.app"
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=2*365)  

  
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    if start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, '%B %d, %Y').date()
        end_date = datetime.strptime(end_date_str, '%B %d, %Y').date()

    base_currencies = {'CAD': CADExchangeRate, 'EUR': EURExchangeRate, 'USD': USDExchangeRate}
    target_currencies = ['CAD', 'USD', 'EUR', 'SEK', 'CHF', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'NZD', 'PHP', 'THB', 'ZAR']

    for base_currency, model in base_currencies.items():
        for target_currency in target_currencies:
            if base_currency != target_currency:
                response = requests.get(f"{base_url}/{start_date}..{end_date}?from={base_currency}&to={target_currency}")
                if response.status_code == 200:
                    data = response.json()
                    rates = data.get('rates', {})
                    for date_str, rate in rates.items():
                        date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        currency_rate = rate.get(target_currency)
                        if currency_rate is not None:
                            try:
                                currency_rate = Decimal(currency_rate)
                                exchange_rate, created = model.objects.get_or_create(
                                    currency=target_currency,
                                    date=date,
                                    defaults={'rate': currency_rate},
                                )
                                if not created:
                                    exchange_rate.rate = currency_rate
                                    exchange_rate.save()
                            except InvalidOperation:
                                logger.error(f"Invalid rate for {target_currency} on {date_str}: {currency_rate}")
                        else:
                            logger.error(f"{target_currency} rate not found for {base_currency} on {date_str}")

    return JsonResponse({'status': 'success'})

