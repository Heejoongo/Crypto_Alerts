from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Alert
from django.urls import reverse
from django.http import JsonResponse
# from .views import fetch_data
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class AlertListView(ListView):
    model = Alert
    template_name = 'alerts/alert_list.html'

class AlertDetailView(DetailView):
    model = Alert
    template_name = 'alerts/alert_detail.html'

    def get_context_data(self, **kwargs):
        # Appellez la méthode implémentée de la super classe pour obtenir le contexte de base
        context = super(AlertDetailView, self).get_context_data(**kwargs)
        # Ajoutez les données de l'API dans le contexte
        context['exchange_data'] = fetch_data()
        return context

class AlertCreateView(CreateView):
    model = Alert
    template_name = 'alerts/alert_form.html'
    fields = ['nom', 'description']

    def get_success_url(self):
        return reverse('alert_detail', kwargs={'pk': self.object.pk})

class AlertUpdateView(UpdateView):
    model = Alert
    template_name = 'alerts/alert_form.html'
    fields = ['nom', 'description']

    def get_success_url(self):
        return reverse('alert_detail', kwargs={'pk': self.object.pk})

class AlertDeleteView(DeleteView):
    model = Alert
    template_name = 'alerts/alert_confirm_delete.html'
    success_url = reverse_lazy('alert_list')
def fetch_data():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    api_key = os.getenv('COINAPI_KEY')
    headers = {
        "X-CoinAPI-Key": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def api_exchange_rate(request):
    data = fetch_data()
    return JsonResponse(data)