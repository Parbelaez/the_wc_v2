from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('',  include('thewcwebpage.urls'), name='thewccwebpage-urls'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
