from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer
from .pagination import BillPagination
from student.models import Student
from .utils import save_study, save_penalty
from rest_framework.permissions import IsAdminUser


class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    pagination_class = BillPagination
    # permission_classes = [IsAdminUser, ]

    def create(self, request, *args, **kwargs):
        self.bill_data(request)
        return super(BillListCreateView, self).create(request, *args, **kwargs)


    @staticmethod
    def bill_data(request):
        from decimal import Decimal
        student_id = request.data.get('student')
        student = Student.objects.get(id=student_id)
        usd = Decimal(request.data.get('usd'))
        eur = Decimal(request.data.get('eur'))
        kgs = Decimal(request.data.get('kgs'))
        type = request.data.get('payment_type')
        if type == 'study':
            save_study(student, usd, eur, kgs)
        elif type == 'penalty':
            days = int(request.data.get('penalty_days'))
            save_penalty(student, days, usd, eur, kgs)






