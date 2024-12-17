from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("up/", include("up.urls")),
    path("", include("pages.urls")),
    path("analytics/", include("analytics.urls")),
    path("ventas/", include("ventas.urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]