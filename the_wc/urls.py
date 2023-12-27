from django.contrib import admin
from django.urls import path
from thewcwebpage.views import my_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  my_page, name='thewcwebpage'),
]
