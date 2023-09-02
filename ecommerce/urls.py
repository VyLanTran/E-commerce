from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('item/', include('item.urls')),
    path('store/', include('store.urls')),
    path('inbox/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
