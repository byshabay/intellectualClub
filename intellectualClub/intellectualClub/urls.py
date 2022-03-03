from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from intellectualClub import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls'), name='home'),
    path('', include('orders.urls'), name='orders'),
]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
