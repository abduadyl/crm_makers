from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from .models import Group, Course
from .serializers import CourseSerializer, GroupSerializer
from .pagination import GroupPagination
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', ]
    filterset_fields = ['course', ]
    # permission_classes = [IsAdminUser, ]
    http_method_names = ['get', 'post', 'patch', ]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', '')
        if ordering == 'student_up':
            data = queryset.first().student.all().order_by('personal_data')
        return queryset


    def get_serializer_context(self):
        return {'action': self.action, 'request': self.request}


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAdminUser, ]
    
