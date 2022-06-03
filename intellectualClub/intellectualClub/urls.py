from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns

from django.views.static import serve as mediaserve
from intellectualClub import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path('', include('main.urls'), name='home'),
    path('', include('orders.urls'), name='orders'),
    path('', include('account.urls'), name='account'),
    path('', include('theblog.urls'), name='blog'),

)
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]
