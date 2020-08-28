from rest_framework import viewsets

from .models import Customer,Book
from .serializers import CustomerSerializer,BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):

        if 'customer_pk' in self.kwargs:
            return Book.objects.filter(
                customer=self.kwargs["customer_pk"]
            )
        else:
            return Book.objects.all()

    @action(methods=['post'], detail=True, url_path='reserve', url_name='reserve')
    def reserve(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if 'customer' not in request.data:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(pk=request.data['customer'])
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['title'] = book.title
        data['status'] = 0
        data['reservation_date'] = datetime.now()

        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)