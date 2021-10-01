from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]