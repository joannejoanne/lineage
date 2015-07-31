"""freightmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns 
from django.contrib import admin    
from . import views 

urlpatterns = patterns('', 
	(r'^admin', admin.site.urls), 
	(r'^$', views.dashboard), 
	(r'^render$', views.render),
    (r'^dashboard$', views.dashboard),
    (r'^getpaths$', views.paths), 
    (r'^getdestination$', views.get_destinations), 
    (r'^Origin-(?P<code>[-\w]+)', views.origin),
    (r'^Destination-(?P<code>[-\w]+)', views.destination),  
    (r'^warehouses$', views.warehouses),
    (r'^freight$', views.home),
    (r'^map$', views.newhome),
    (r'^oldmap$', views.oldhome),
    (r'^sample$', views.sample),

    (r'^expanded$', views.home_expanded),
    (r'^warehouseinit$', views.warehouse_init),
    (r'^warehousemap$', views.warehousemap)
)

