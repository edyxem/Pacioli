from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('users/', include('users.urls')),
    path('recettes/', include('recettes.urls')),
    path('depenses/', include('depenses.urls')),
    path('tiers/', include('tiers.urls')),
    path('rapports/', include('rapports.urls')),
]