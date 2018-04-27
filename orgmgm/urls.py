from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns=[
    url(r'^$',TemplateView.as_view(template_name='orgmgm/home.html'), name='home'),
    url(r'^dashboard/$', TemplateView.as_view(template_name='orgmgm/dashboard/overview.html'), name='dashboard_overview'),
    url(r'^resources/$',views.resource, name='resources'),
    url(r'^faq/$',views.faq, name='faq'),
    url(r'^activity/$', views.activity_list, name='activity_list'),
    url(r'^dashboard/data$', views.dashboard_data, name='dashboard_data'),
    url(r'^activity/add/$', views.activity_add, name='activity_add'),
    url(r'^activity/detail/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activity/edit/(?P<pk>\d+)/$', views.activity_edit, name='activity_edit'),
    url(r'^activity/delete/(?P<pk>\d+)/$', views.activity_delete, name='activity_delete'),
    url(r'^activity/search/$', views.activity_search, name='activity_search'),
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

