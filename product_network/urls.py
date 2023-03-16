from django.contrib import admin
from django.urls import path, include

from core.views import EnterprisesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('core.urls')),
    path('goods/', include('goods.urls')),
    path('enterprises', EnterprisesView.as_view()),
]
