from basic_app import views
from django.conf.urls import url

#TEMPLATE TAGGING
app_name = 'basic_app' #href will look for this name, the variable name should be app_name only.

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]