from rest_framework import generics, viewsets
from .models import Group, Course
from .serializers import CourseSerializer, GroupSerializer
from .pagination import GroupPagination
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAdminUser, ]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]
    # permission_classes = [IsAdminUser, ]
    http_method_names = ['get', 'post', ]

    def get_serializer_context(self):
        return {'action': self.action, 'request': self.request}