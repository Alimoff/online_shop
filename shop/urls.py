from tokenize import Single
from django.urls import path
from .views import CustomersView,SingleCustomer

urlpatterns = [
    path('list/',CustomersView.as_view()),
    path('list/<int:id>/',SingleCustomer.as_view()),
]