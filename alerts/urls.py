
from django.urls import path
from .views import (
    AlertListView,
    AlertDetailView,
    AlertCreateView,
    AlertUpdateView,
    AlertDeleteView,
    api_exchange_rate
)

urlpatterns = [
    path('', AlertListView.as_view(), name='alert_list'),
    path('<int:pk>/', AlertDetailView.as_view(), name='alert_detail'),
    path('add/', AlertCreateView.as_view(), name='alert_add'),
    path('<int:pk>/update/', AlertUpdateView.as_view(), name='alert_update'),
    path('<int:pk>/delete/', AlertDeleteView.as_view(), name='alert_delete'),
    path('api/exchange_rate/', api_exchange_rate, name='api_exchange_rate'),

]
