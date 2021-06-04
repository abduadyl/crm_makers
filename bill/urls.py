from django.urls import path
from .views import BillListCreateView

urlpatterns = [
    path('bill/', BillListCreateView.as_view()),
]