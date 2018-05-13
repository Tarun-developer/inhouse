


from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^siteadmin/', admin.site.urls),
    url(r'^dashboard/', include('search.urls')),
    url(r'^owner/',include('owner.urls')),
    url(r'^scrap/',include('scrap.urls')),
    
    # url(r'^', include('login.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
