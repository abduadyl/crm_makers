from rest_framework.pagination import PageNumberPagination


class BillPagination(PageNumberPagination):
    page_size = 10