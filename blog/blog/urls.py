from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog_app.urls')),
    path('members/',include('django.contrib.auth.urls')), # this handel login and logout links and urls
    path('members/',include('members.urls')),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
