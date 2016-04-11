from django.conf.urls import url

from booking import views


app_name = 'booking'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'search/', views.search_results, name='search'),
]
