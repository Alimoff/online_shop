from django.urls import path
from .views import CustomerView

urlpatterns = [
    path('list/',CustomerView.as_view())
]