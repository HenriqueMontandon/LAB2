from django.urls import path

from . import views

app_name = 'destinos'
urlpatterns = [
    path('', views.DestinoListView.as_view(), name='index'), 
    path('search/', views.search_destinos, name='search'),
    path('create/', views.create_destino, name='create'),
     path('lists/', views.RoteiroListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
    path('<int:pk>/', views.DestinoDetailView.as_view(), name='detail'),
]