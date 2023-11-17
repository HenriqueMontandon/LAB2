from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.listPosts.as_view(), name='index'), 
    path('<int:post_id',views.DetailPost.as_view(), name='detail'),
    path('<int:post_id>/delete', views.DeletePost.as_view(), name='delete'),
    path('<int:post_id>/edit', views.EditPost.as_view(),name='edit'),
    path('create/', views.CreatePost.as_view(), name='create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)