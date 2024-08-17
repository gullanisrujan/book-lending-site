from django.urls import path,include
from django.conf import settings
from . import views
urlpatterns = [
    path('exchange',views.exchange),
    path('lend',views.lend),
    path('buy',views.buy)
]
