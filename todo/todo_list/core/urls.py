from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path('update', views.upload, name='update'),
    
    path('edit/<int:pk>/', views.update , name='edit'),
    path('delet/<int:pk>/',views.deletel , name='delet')
    
]
