from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.dashboard_overview, name='dashboard_overview'),
    url(r'^activity/add/$', views.activity_add, name='activity_add'),
    url(r'^activity/detail/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^kontakt/$', views.kontakt_list, name='kontakt_list'),
    url(r'^kontakt/search/$', views.kontakt_search, name='kontakt_search'),
    url(r'^kontakt/add/$', views.kontakt_add, name='kontakt_add'),
    url(r'^kontakt/detail/(?P<pk>\d+)/$', views.kontakt_detail, name='kontakt_detail'),
    url(r'^kontakt/edit/(?P<pk>\d+)/$', views.kontakt_edit, name='kontakt_edit'),
    url(r'^kontakt/delete/(?P<pk>\d+)/$', views.kontakt_delete, name='kontakt_delete'),
    url(r'^organisation/$', views.organisation_list, name='organisation_list'),
    url(r'^organisation/search/$', views.organisation_search, name='organisation_search'),
    url(r'^organisation/add/$', views.organisation_add, name='organisation_add'),
    url(r'^organisation/detail/(?P<pk>\d+)/$', views.OrganisationDetail.as_view(), name='organisation_detail'),
    url(r'^organisation/edit/(?P<pk>\d+)/$', views.organisation_edit, name='organisation_edit'),
    url(r'^organisation/delete/(?P<pk>\d+)/$', views.organisation_delete, name='organisation_delete'),
]   

