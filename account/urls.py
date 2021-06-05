from django.urls import path
from account.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
]