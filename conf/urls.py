from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.contrib import admin

urlpatterns = (
        [
            path('mdt-admin/', admin.site.urls),
        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = 'Hydra'
admin.site.site_title = 'Hydra'
admin.site.index_title = 'Hydra Admin Panel'
