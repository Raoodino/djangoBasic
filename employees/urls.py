from django.urls import path
from . import views

urlpatterns = [
    #dynamic value for primary key
    path('<int:pk>/', views.employee_detail, name = 'employee_detail'),
]