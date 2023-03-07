from django.contrib import admin
from empresa.models import Company, Customer, Place, Payment, Scheduling

class Companys(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Company, Companys)

class Customers(admin.ModelAdmin):
    list_display = ('id', 'name','company')
    list_display_links = ('id', 'name','company')
    search_fields = ('name',)
admin.site.register(Customer, Customers)

class Places(admin.ModelAdmin):
    list_display = ('id', 'name','company')
    list_display_links = ('id', 'name','company')
    search_fields = ('name',)
admin.site.register(Place, Places)

class Payments(admin.ModelAdmin):
    list_display = ('id', 'total_amount', 'paid_amount', 'payment_type')
    list_display_links = ('id',)
    search_fields = ('id',)
admin.site.register(Payment,Payments)

class Schedulings(admin.ModelAdmin):
    list_display = ('id', 'date', 'entry_time', 'exit_time', 'customer', 'place', 'payment', 'company')
    list_display_links = ('id',)
    search_fields = ('id',)
admin.site.register(Scheduling, Schedulings)