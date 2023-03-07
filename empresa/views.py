from rest_framework import viewsets, generics
from empresa.models import Company, Customer, Place, Payment, Scheduling
from empresa.serializer import CompanySerializer, CustomerSerializer, PlaceSerializer, PaymentSerializer, SchedulingSerializer, HorariosClientesSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """Exibindo todas as empresas"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    """Exibindo todas as quadras diponívels"""
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """Exibindo toda a tabela de pagamentos"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class SchedulingViewSet(viewsets.ModelViewSet):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer

class HorariosClientes(generics.ListAPIView):
    """Listando os horários"""
    def get_queryset(self):
        queryset = Scheduling.objects.filter(customer_id=self.kwargs['pk'])
        return queryset
    serializer_class = HorariosClientesSerializer