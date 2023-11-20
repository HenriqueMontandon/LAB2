from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.listPosts.as_view(), name='index'), 
    path('<int:pk>',views.DetailPost.as_view(), name='detail'),
    path('<int:pk>/delete', views.DeletePost.as_view(), name='delete'),
    path('<int:pk>/edit', views.EditPost.as_view(),name='edit'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('createCategory/', views.CreateCategorieView.as_view(), name='createCategorie'),
    path('category/<int:pk>/delete', views.deleteCategorieView.as_view(), name='deleteCategory'),
    path('listCategories/', views.listCategories.as_view(), name='listCategories')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)