from django.conf.urls import url

from booking import views


app_name = 'product'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
