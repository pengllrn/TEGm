"""TEGm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

import TEGApp.views as tv
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Login/(?P<user_id>[A-Za-z0-9]+)/(?P<user_pwd>[A-Za-z0-9]+)/$',tv.ard_login),
    url(r'^TEGApp/', include('TEGApp.urls')),
    ##url(r'^server_login/fruit/$',tv.getFruits),
    url(r'^getdeviceinfo/$',tv.getDeviceInfo),
    url(r'^getdevice/$',tv.get_school_building_room),
    url(r'^getdevicedetail/$',tv.get_detail_device),
    url(r'^damageapply/$',tv.device_damage_apply),
    url(r'^searchdevicebynum/$',tv.search_device_bynum),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
