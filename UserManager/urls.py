from django.conf.urls import patterns, include, url
from Manager import views
from django.contrib.auth.views import login

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
    url(r'^registe/$', views.Registe),
    url(r'^login/$', views.Login),
    url(r'^account/login$', login, {'template_name': 'login_new.html'}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/css'}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/js'}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/img'}),
    url(r'^ico/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/ico'}),
    url(r'^logout/$', views.Logout),
    url(r'^index$', views.Index),
    url(r'^detail/(\d+)/$', views.BugDetail),
)
