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
        if action == 'retrieve':
            representation['students'] = StudentSerializer(Student.objects.filter(group=instance.id), many=True).data
        return representation
