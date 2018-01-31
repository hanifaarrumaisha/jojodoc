"""jojodoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
import jojo_layout.urls as index
from jojo_layout.views import index as layout
from jojo_style.views import index as style
from jojo_component.views import index as component

app_name='jojodoc'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include(index, namespace='index')),
    url(r'^layout', layout, name='layout'),
    url(r'^style', style, name='style'),
    url(r'^component', component, name='component'),
]
