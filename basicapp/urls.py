from django.conf.urls  import url
from . import views


app_name = 'basicapp'

urlpatterns = [

    url(r'^realtive', views.relative, name='relative'),
    url(r'^other', views.other, name='other'),

]


