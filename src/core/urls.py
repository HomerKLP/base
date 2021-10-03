from typing import Tuple, Any

from django.contrib import admin
from django.urls import path

from .helpers.drf_yasg import schema_view
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns: Tuple[Any, ...] = (
    path(route='admin/', view=admin.site.urls),
    path(
        route='docs/', name='docs',
        view=schema_view.with_ui('redoc', cache_timeout=0),
    ),
)

if DEBUG:
    from django.conf.urls.static import static

    urlpatterns += tuple(
        static(prefix=MEDIA_URL, document_root=MEDIA_ROOT),
    )
