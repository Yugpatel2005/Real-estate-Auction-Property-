"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',views.aboutpage),
    path("login",views.loginpage),
    path("register1",views.registerpage),
    path("index",views.indexpage),
    path("",views.index6page),
    path("fetchregister",views.fetchregister),
    path("fetchlogindata",views.fetchlogindata),
    path("logout",views.logout),
    path("index-3",views.index3page),
    path("account",views.accountpage),
    path("add-listing",views.addlistingpage),
    path("fetchaddproperty", views.fetchaddproperty),
    path("product-details/<int:id>",views.productdetailspage),
    path("deleteitem/<int:id>", views.deleteitem),
    path("property-search",views.property_search),
    path("shop-list",views.shoplistpage),
    path("cart",views.cartpage),
    path("forgotpass",views.forgotpage),
    path("rentproperty",views.rentproperty),
    path("propertyforsale",views.propertyforsale),
    path("insertintocart",views.insertintocart),
    path("shop",views.shop),
    path("allproperty",views.allproperty),
    path('pricing', views.pricing, name='pricing'),
    path('create_order/<int:plan_id>', views.create_order, name='create_order'),
    path('payment_success', views.payment_success, name='payment_success'),
    path("add_renting/<int:renting_id>/", views.add_renting, name="add_renting"),
    path("verify_payment/<int:donation_id>/", views.verify_payment, name="verify_payment"),
    path("inquiry/<int:property_id>", views.inquiry_form, name="inquiry_form"),
    path("forgotpassword", views.forgotpassword),
    path("myrentprop",views.myrentprop),
    path("myrent",views.myrent),
    path("myauctprop",views.myauctprop),
    path("myinquiry",views.myinquiry),
    path("updatepass", views.updatepass),
    path('contact',views.contactpage),
    path('fetchcontact',views.fetchcontact),
    path('fetchfeedback',views.fetchfeedback),
    path('feedback',views.feedbackpage)


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

