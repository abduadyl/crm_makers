from rest_framework import serializers
from .models import Group, Course
from student.serializers import StudentSerializer
from student.models import Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        exclude = ('last_check', )

    def to_representation(self, instance):
        representation = super(GroupSerializer, self).to_representation(instance)
        action = self.context.get('action')
        ordering = self.context['request'].GET.get('ordering', '')
        if action == 'retrieve':
            representation['course_title'] = instance.course.type
            if ordering == 'student_down':
                students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-personal_data'), many=True).data
            elif ordering == 'student_up':
                students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('personal_data'), many=True).data
            representation['students'] = students
        elif action == 'list':
            representation['course_title'] = instance.course.type
        return representation
