from django.urls import path
from cars import views

urlpatterns = [
    path('', views.CarList.as_view()),
    path('<int:pk>/', views.CarDetails.as_view()),
]
