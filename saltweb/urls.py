#coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from saltstack.views import *
from line.views  import *
from fee.views import *
from demo.views import *
from django.contrib.auth.views import login,logout
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^index\.html/$',indexhtml),
    (r'^ssh\.html/$',sshhtml),
    (r'^excel/$',excel),
    (r'^monitor\.html/$',monitorhtml),
    (r'^zabbix\.html/$',zabbixhtml),
    (r'^salt\.html/$',salthtml),
    (r'^ops\.html/$',opshtml),
    (r'^admin\.html/$',adminhtml),
    (r'^fee\.html/$',feehtml),
    (r'^line\.html/$',linehtml),
    (r'^area\.html/$',areahtml),
    (r'^compose\.html/$',composehtml),
    (r'^chart\.html/$',charthtml),
    (r'^ldzw\.html/$',ldzwhtml),
    (r'^cqb\.html/$',cqbhtml),
    (r'^tkzz\.html/$',tkzzhtml),
    (r'^ldzw/$',ldzw),
    (r'^cqb/$',cqb),
    (r'^tkzz/$',tkzz),
    (r'^showall/$',showall),
    (r'^ldzwarea\.html/$',ldzwareahtml),
    (r'^cqbarea\.html/$',cqbareahtml),
    (r'^tkzzarea\.html/$',tkzzareahtml),
    (r'^stack\.html/$',stackhtml),
    (r'^ldzwbar\.html/$',ldzwbarhtml),
    (r'^cqbbar\.html/$',cqbbarhtml),
    (r'^tkzzbar\.html/$',tkzzbarhtml),
    (r'^chartbar\.html/$',chartbarhtml),
    (r'^chartbar1\.html/$',chartbar1html),
    #(r'^acounts/login/$',login),
    #(r'^acounts/logout/$',logout),
    #(r'^main/$',main),
    (r'^account/$',denglu),
    (r'^login/$',login_view),
    (r'^logout/$',logout_view),
    (r'^test/$',test),
    (r'^debugg/$',debugg),
    (r'^ldzwdate/$',ldzwdate),
    (r'^update/$',update),

    (r'^accountline/$',dengluline),
    (r'^loginline/$',login_viewline),
    (r'^logoutline/$',logout_viewline),
    (r'^test/$',test),
    (r'^debugg/$',debugg),
    (r'^ldzwdateline/$',ldzwdateline),
    (r'^updateline/$',updateline),
    (r'^ldzwline/$',ldzwline),
    (r'^cqbline/$',cqbline),
    (r'^tkzzline/$',tkzzline),
    (r'^showallline/$',showallline),
    (r'^showline/$',showline),
    (r'^showlinedate/$',showlinedate),
    (r'^table/$',table),
    (r'^information/$',information),

    # Examples:
    # url(r'^$', 'saltweb.views.home', name='home'),
    # url(r'^saltweb/', include('saltweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
