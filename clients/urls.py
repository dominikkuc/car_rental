from django.urls import path
from clients import views

urlpatterns = [
    path('', views.ClientList.as_view()),
    path('<int:pk>/', views.ClientDetails.as_view()),
]
