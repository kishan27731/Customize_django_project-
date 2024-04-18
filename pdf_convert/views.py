import importlib.machinery
import importlib.util
from django.shortcuts import render
from multiprocessing import context
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from des.models import Order, OrderItem,product
from des.views import products

#user##########################################start#
def show_user(request):
    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'pdf_convert/user_showinfo.html', context)


def user_pdf_view(request):
    users = User.objects.all()
    template_path = 'pdf_convert/user_printer.html'
    context = {
        'users': users
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="userreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#user##########################################end#
def order_details_show(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }

    return render(request, 'pdf_convert/order_showinfo.html', context)


def order_details_pdf(request):
    orders = Order.objects.all()
    template_path = 'pdf_convert/order_create_pdf.html'
    
    context = {
        'orders': orders
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="OrderReport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#order##########################################end#

def product_details_show(request):
    products = product.objects.all()

    context = {
        'products': products
        
    }

    return render(request, 'pdf_convert/product_showinfo.html', context)

def product_details_pdf(request):
    products = product.objects.all()
    template_path = 'pdf_convert/product_create_pdf.html'
    
    context = {
        'products': products
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ProductsReport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def invoicedetail(request):
    template_path = 'pdf_convert/invoicedetail.html'
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id=uid)
    orders = Order.objects.filter(user=user)
    order_items = OrderItem.objects.filter(order__in=orders)
    context = {
        'orders': orders,
        'order_items': order_items,
        'user': user,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





 