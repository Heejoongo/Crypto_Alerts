from django.urls import reverse_lazy
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from dotenv import load_dotenv
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alert
from .forms import AlertForm
from django.contrib import messages
from django.utils.dateparse import parse_datetime



load_dotenv()
@login_required
def alert_detail(request, pk):
    alert = get_object_or_404(Alert, pk=pk, user=request.user)
    # rate = fetch_data(alert.base, alert.quote)
    # print(rate)
    # return render(request, 'alerts/alert_detail.html', {'alert': alert, 'rate': rate, 'base': alert.base})
    return render(request, 'alerts/alert_detail.html', {'alert': alert, 'threshold_value': alert.threshold_value})


@login_required
def alert_list(request):
    alerts = Alert.objects.filter(user=request.user)
    return render(request, 'alerts/alert_list.html', {'alerts': alerts})


@login_required
def alert_create(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            return redirect('alerts:alert_detail', pk=alert.id)
    else:
        form = AlertForm()

    return render(request, 'alerts/alert_form.html', {'form': form})


@login_required
def alert_update(request, pk):
    alert = get_object_or_404(Alert, pk=pk, user=request.user)  # Get the Alert object, ensuring the current user owns it
    if request.method == 'POST':
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.save()
            return redirect('alerts:alert_detail', pk=alert.pk)
    else:
        form = AlertForm(instance=alert)

    return render(request, 'alerts/alert_form.html', {'form': form, 'alert': alert})


@login_required
def alert_delete(request, pk):
    alert = get_object_or_404(Alert, pk=pk, user=request.user)
    if request.method == 'POST':
        alert.delete()
        messages.success(request, 'Alert deleted successfully!')
        return redirect('alerts:alert_list')

@login_required
def fetch_data(base, quote):
    url = f"https://rest.coinapi.io/v1/exchangerate/{base}"
    api_key = os.getenv('COINAPI_KEY')
    headers = {"X-CoinAPI-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'rates' in data:
        for rate_info in data['rates']:
            if rate_info.get('asset_id_quote') == quote:
                return rate_info.get('rate')

@login_required
def fetch_rate(request):
    base = request.GET.get('base')
    quote = request.GET.get('quote')
    rate = fetch_data(base, quote)
    if rate is not None:
        return JsonResponse({'rate': rate})
    else:
        return JsonResponse({'rate': 0})


@csrf_exempt  # Only use this if you know what you are doing regarding CSRF protection!
@require_POST
@login_required
def update_rate(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        rate = data.get('rate')
        updated_at_str = data.get('updated_at')
        updated_at = parse_datetime(updated_at_str)
        alert = get_object_or_404(Alert, pk=pk, user=request.user)
        alert.rate = rate
        alert.updated_at = updated_at
        alert.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
