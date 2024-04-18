
# Register your models here.
from django.contrib import admin
from des.models import Images, Order, OrderItem, Tag, categorie,brand,color, contactus, filter_price, product,profile
# Register your models here.
class ImagesTublerinline(admin.TabularInline):
    model=Images
class TagTublerinline(admin.TabularInline):
    model=Tag
class productadmin(admin.ModelAdmin):
    inlines=[ImagesTublerinline,TagTublerinline]
    


class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem


    
class OrderAdmin(admin.ModelAdmin):
    inlines =[OrderItemTublerinline]
    list_display=['firstname','email','phone','Paymentid','Paid','date']
    search_fields=['email','Paymentid','firstname']


admin.site.register(categorie)
admin.site.register(brand)
admin.site.register(color)
admin.site.register(product,productadmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(contactus)
admin.site.register(filter_price)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(profile)
