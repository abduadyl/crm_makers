from django.urls import path
from .views import CourseListCreateView

urlpatterns = [
    path('course/', CourseListCreateView.as_view()),
]