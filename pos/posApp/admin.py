from django.contrib import admin
from posApp.models import Category, Products, Sales, salesItems, Inventory, Customer, Supplier

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Supplier)

# admin.site.register(Employees)


#class SupplierAdmin(admin.ModelAdmin):
#    list_display = ['user', 'name', 'address', 'created_date']
#admin.site.register(Supplier, SupplierAdmin)