from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login',views.login),
    path('register',views.register),
    path('dashboard',views.dashboard),
    path('search',views.search),
    path('logout',views.logout),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)