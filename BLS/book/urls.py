from django.urls import path
from . import views
urlpatterns = [
    path('add', views.add),
    path('delete', views.delete),
    path('eadd', views.eadd),
    path('edelete', views.edelete),
]
