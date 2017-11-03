"""uwcbewerbung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from orgmgm import views as myviews

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/orgmgm/')),
    url(r'^orgmgm/', include('orgmgm.urls'), name='orgmgm'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'orgmgm/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    #url(r'^signup/$', myviews.signup, name='signup'),
]

