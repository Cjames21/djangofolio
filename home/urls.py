from django.conf.urls import url
from . import views

urlpatterns = [
    url('thank_you/$', views.thank_you, name='thank_you'),
    url('thank_you.html', views.thank_you, name='thank_you'),
    url('contact_me.html', views.contact_me, name='contact_me'),
    url('contact_me/$', views.contact_me, name='contact_me'),
    url('index/contact_me/', views.contact_me, name='index'),
    url('portfolio', views.portfolio, name='portfolio'),
    url('portfolio/$', views.portfolio, name='portfolio'),
    url('index/', views.index, name='index'),
    url('', views.index, name='index'),
]
