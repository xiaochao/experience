from django.conf.urls import patterns, include, url
from Manager import views
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
    url(r'^registe/$', views.Registe),
    url(r'^login/$', views.Login),
    url(r'^account/login$', login, {'template_name': 'login_new.html'}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/css'}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/js'}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/supertool/projects/www/UserManager/assets/images'}),
    url(r'^account/logout/$', logout),
    url(r'^index$', views.Index),
)
