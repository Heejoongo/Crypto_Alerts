from django.urls import path
from . import views

app_name = 'alerts'

urlpatterns = [
    path('', views.alert_list, name='alert_list'),

    path('create/', views.alert_create, name='alert_create'),

    path('<int:pk>/', views.alert_detail, name='alert_detail'),

    path('<int:pk>/update/', views.alert_update, name='alert_update'),

    path('<int:pk>/delete/', views.alert_delete, name='alert_delete'),

    path('fetch-rate/', views.fetch_rate, name='fetch-rate'),

    path('update-rate/<int:pk>/', views.update_rate, name='update_rate'),
]
