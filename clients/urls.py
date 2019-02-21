from django.urls import path
from clients import views

urlpatterns = [
    path('clients/', views.ClientListView.as_view()),
    path('clients/<int:pk>/', views.ClientDetails.as_view()),
]
