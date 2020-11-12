from django.urls import path
from . import views

app_name ='mangas'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/book/', views.BookView.as_view(), name='book'),
]