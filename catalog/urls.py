from django.urls import path
from django.urls import include, re_path
from . import views
app_name='catalog'
urlpatterns = [ 
    re_path(r'^$',views.Index.as_view(),name='index'),

]