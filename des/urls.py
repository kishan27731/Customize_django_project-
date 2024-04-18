from tkinter import Place
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 #path('admin/',admin.site.urls),
    path("",views.home,name="home"),
    path('base/',views.base,name="base"),
    path('product/',views.products,name="product"),
    path('search/',views.search,name="search"),
    path('product/<str:id>',views.products_detail,name="single_product"),
    path('contact/',views.contact_page,name="contact"),
    path('register/',views.HandleRegister,name="register"),
    path('login/',views.HandleLogin,name="login"),
    path('logout/',views.HandleLogout,name="logout"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('messages/',views.message,name="messages"),
    path('prof/',views.profile,name="prof"),
    path('forget/',views.forgetpassword,name="forget"),
    path('system/',views.systembuilder,name="system"),
    path('success/',views.changedpasswd,name="successfull"),
    path('unsuccess/',views.error,name="unsuccessfull"),
    path('nouser/',views.nouser,name="nouser"),
    path('allorders/',views.all,name="allorders"),

    

#add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_details/',views.cart_detail,name='cart_details'),
  path('system/<int:id>/', views.systembuilder, name='systembuilder'),

    path('cart/checkout/',views.Check_out,name="checkout"),
    path('cart/placeorder/',views.Place_order,name="place_order"),
    path('forget/success.html',views.changedpasswd,name="success"),
    path('forget/unsuccess.html',views.error,name="unsuccessfull"),
    path('forget/nouser.html',views.nouser,name="nouser"),
    path('success',views.success,name="success"),
    path('your-order',views.your_order,name="your_order"),
    path('allorder',views.all,name="allorder"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)