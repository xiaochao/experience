from django.conf.urls import patterns, include, url
from Manager.views import Registe,Login
from django.contrib.auth.views import login,logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UserManager.views.home', name='home'),
    # url(r'^UserManager/', include('UserManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^registe/$', Registe),
    url(r'^login/$', Login),
    url(r'^account/login/$', login, {'template_name': 'login_new.html'}),
    url(r'^account/logout/$', logout),
)
