from django.conf.urls import url
from . import views as tasma

urlpatterns = [
    url(r'^$', tasma.index, name='index'),
    url(r'^import/$', tasma.import_data, name='import'),       
]
