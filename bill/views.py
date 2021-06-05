from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer
from .pagination import BillPagination
from student.models import Student
from .utils import save_data
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
        save_data(student, usd, eur, kgs)






