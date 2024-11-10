from django.urls import path
from . import views

urlpatterns = [

    path('<int:pk>/', views.employee_detail, name='employee_detail') 
    #nell'url dopo la parte employees il valore verrà passato come parametro intero di nome pk alla funzione. Viene catturato il valore della partefinale dell'url
]