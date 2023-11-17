from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.listPosts.as_view(), name='index'), 
    path('<int:post_id',views.DetailPost.as_view(), name='detail'),
    path('<int:post_id>/delete', views.DeletePost.as_view(), name='delete'),
    path('<int:post_id>/edit', views.EditPost.as_view(),name='edit')
]