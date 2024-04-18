from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('showusers', views.show_user, name='showusers'),
    path('orderdetail', views.order_details_show, name='orderdetail'),
    path('productdetail', views.product_details_show, name='productdetail'),
     path('invoicedetail', views.invoicedetail, name='invoicedetail'),
  
##################################################################################

    path('createpdfusers', views.user_pdf_view, name='createpdfusers'),
    path('createpdforders', views.order_details_pdf, name='createpdforders'),
    path('createpdfproducts', views.product_details_pdf, name='createpdfproducts'),
    path('createpdfinvoice', views.invoicedetail, name='createpdforinvoice'),
    
]