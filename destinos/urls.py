from django.urls import path

from . import views

app_name = 'destinos'
urlpatterns = [
    path('', views.DestinoListView.as_view(), name='index'), 
    path('search/', views.search_destinos, name='search'),
    path('create/', views.create_destino, name='create'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
    path('<int:destino_id>/', views.detail_destino, name='detail'),
    path('lists/<int:pk>/', views.RoteiroDetailView, name='roteiro'),
    path('lists/update/<int:pk>/', views. update_Roteiro.as_view(), name="update"),
    path('lists/delete/<int:pk>', views.delete_Roteiro.as_view(), name ='delete')
]