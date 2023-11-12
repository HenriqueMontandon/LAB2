from django.urls import path

from . import views

app_name = 'destinos'
urlpatterns = [
    path('', views.list_destinos, name='index'), 
    path('search/', views.search_destinos, name='search'),
    path('create/', views.create_destino, name='create'),
    path('<int:destino_id>/', views.detail_destino, name='detail'),
]