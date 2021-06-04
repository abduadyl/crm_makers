from rest_framework import serializers
from .models import Student
from bill.serializers import BillSerializer
from bill.models import Bill


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(StudentSerializer, self).to_representation(instance)
        action = self.context.get('action')
        if action == 'list':
            representation['group_title'] = instance.group.title
        elif action == 'retrieve':
            representation['group_title'] = instance.group.title
            representation['bills'] = BillSerializer(Bill.objects.filter(student=instance.id), many=True).data
        return representation


class StudentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('course_price', 'payment_month', 'total_paid',
                   'credit_balance', 'reserve', 'created', 'freeze_date')

    def to_representation(self, instance):
        representation = super(StudentCreateUpdateSerializer, self).to_representation(instance)
        representation['group'] = instance.group.title
        return representation