"""Payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app_payment import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('show_add_payment/',views.showPayment,name='show_add_payment'),
    path('add_payment/',views.addPayment,name='add_payment'),
    path('show_payment/',views.showEditPayment,name='show_payment'),
    path('edit_payment/',views.editPayment,name='edit_payment'),
    path('del_payment/',views.deletePayment,name='del_payment'),
    path('show_search_payment/',views.show_searchPayment,name='show_search_payment'),
    path('search_payment/',views.searchPayment,name='search_payment'),
]