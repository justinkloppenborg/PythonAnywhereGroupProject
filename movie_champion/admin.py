from django.contrib import admin

from .models import Movie, Customer, Service, Product


class MovieList(admin.ModelAdmin):
    list_display = ('movie_name', 'staring')
    list_filter = ('movie_name', 'staring')
    search_fields = ('movie_name',)
    ordering = ['movie_name']


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'phone_number')
    list_filter = ('cust_name',)
    search_fields = ('cust_name',)
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'service_category', 'setup_time')
    list_filter = ( 'cust_name', 'setup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'pickup_time')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Movie)
admin.site.register(Customer)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)
