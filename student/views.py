from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer, StudentCreateUpdateSerializer
from .pagination import StudentPagination
from group.models import Group
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    pagination_class = StudentPagination
    # permission_classes = [IsAdminUser, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['personal_data', 'group__title', ]
    http_method_names = ['get', 'post', 'patch', ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer = StudentSerializer
        elif self.request.method in ['PATCH', 'POST']:
            serializer = StudentCreateUpdateSerializer
        return serializer

    def get_serializer_context(self):
        return {'action': self.action, 'request': self.request}

    def create(self, request, *args, **kwargs):
        self.plus_student(request)
        return super(StudentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.minus_student(request, *args, **kwargs)
        return super(StudentViewSet, self).update(request, *args, **kwargs)

    @staticmethod
    def plus_student(request):
        group_id = request.data.get('group')
        group = Group.objects.get(id=group_id)
        group.total_students += 1
        group.save()

    @staticmethod
    def minus_student(request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Student.objects.get(id=student_id)
        group = Group.objects.get(id=student.group.id)
        if request.data.get('freeze_status') is True or request.data.get('freeze_status') == 'true':
            group.total_students -= 1
            group.save()



