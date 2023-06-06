from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.settings import common as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/", include("apps.product.urls")),
    path("user/", include("apps.users.urls")),
    path("order/", include("apps.orders.urls")),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
