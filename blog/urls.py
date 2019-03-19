from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from django.contrib import admin
app_name="blogs"
urlpatterns=[
 path('admin/', admin.site.urls), 
 path("",include('blogs.urls')),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)