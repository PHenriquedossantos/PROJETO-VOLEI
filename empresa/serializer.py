from rest_framework import serializers
from empresa.models import Company, Customer, Place, Payment, Scheduling

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'company']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'company']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'PAYMENT_TYPES', 'total_amount', 'paid_amount', 'payment_type']

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = ['id', 'date', 'entry_time', 'exit_time', 'customer', 'place', 'payment', 'company']


class HorariosClientesSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.name')
    place = serializers.ReadOnlyField(source='place.name')
    payment = serializers.ReadOnlyField(source='payment.payment_type')
    company = serializers.ReadOnlyField(source='company.company.name')
    class Meta:
        model = Scheduling
        fields = fields = ['id', 'date', 'entry_time', 'exit_time', 'customer', 'place', 'payment', 'company']
        #127.0.0.0.8000/customer/id_customer/horario






