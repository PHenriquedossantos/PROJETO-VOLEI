from django.contrib import admin
from django.urls import path, include
from empresa.views import CompanyViewSet, CustomerViewSet, PlaceViewSet, PaymentViewSet, SchedulingViewSet, HorariosClientes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='Company')
router.register('customer', CustomerViewSet, basename='Customer')
router.register('place', PlaceViewSet, basename='Place')
router.register('payment', PaymentViewSet, basename='Payment')
router.register('scheduling', SchedulingViewSet, basename='Scheduling')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('customer/<int:pk>/horarios', HorariosClientes.as_view())
]

#127.0.0.0.8000/customer/id_customer/horario