from django.contrib import admin
import re
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('useradmission/', include("useradmission.urls")),
    path('property/', include("property.urls")),
    path('landlord/', include("landlord.urls")),
    path('tenant/', include("tenant.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
