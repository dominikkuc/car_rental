from django.urls import path
from orders import views

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('<int:pk>/', views.OrderDetails.as_view()),
]
