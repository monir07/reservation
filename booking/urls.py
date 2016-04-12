from django.conf.urls import url

from booking import views


app_name = 'booking'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^booking/', views.book_ticket, name='book_ticket'),
    url(r'^ticket/(?P<pk>[0-9]+)/$', views.GetTicket.as_view(), name='get_ticket'),
]
