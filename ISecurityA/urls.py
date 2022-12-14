from django.urls import path

from . import views

urlpatterns = [
    path('', views.search),
    path('dados/<int:pk>/', views.dados_sensiveis, name='dados_sensiveis'),
]

app_name = 'ISecurityA'
