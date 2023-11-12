from django.urls import path

from . import views

app_name = 'destinos'
urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'), 
    path('search/', views.search_destinos, name='search'),
    path('create/', views.create_destino, name='create'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
]