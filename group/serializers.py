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
            representation['students'] = self.ordering(ordering, instance)
        elif action == 'list':
            representation['course_title'] = instance.course.type
        return representation


    @staticmethod
    def ordering(ordering, instance):
        if ordering == 'student_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-personal_data'),
                                         many=True).data
        elif ordering == 'student_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('personal_data'),
                                         many=True).data
        elif ordering == 'payment_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('payment_month'),
                                         many=True).data
        elif ordering == 'payment_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-payment_month'),
                                         many=True).data
        elif ordering == 'total_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('total_paid'),
                                         many=True).data
        elif ordering == 'total_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-total_paid'),
                                         many=True).data
        elif ordering == 'credit_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('credit_balance'),
                                         many=True).data
        elif ordering == 'credit_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-credit_balance'),
                                         many=True).data
        elif ordering == 'credit_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-credit_balance'),
                                         many=True).data
        elif ordering == 'credit_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-credit_balance'),
                                         many=True).data
        elif ordering == 'reserve_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('reserve'), many=True).data
        elif ordering == 'reserve_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-reserve'), many=True).data
        elif ordering == 'discount_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('discount'), many=True).data
        elif ordering == 'discount_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-discount'), many=True).data
        elif ordering == 'course_down':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('course_price'), many=True).data
        elif ordering == 'course_up':
            students = StudentSerializer(Student.objects.filter(group=instance.id).order_by('-course_price'), many=True).data
        else:
            students = StudentSerializer(Student.objects.filter(group=instance.id), many=True).data
        return students





