from django.conf.urls import url, include
from formpatterns import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name='formpatterns'

urlpatterns = [
    url(r'^$', views.FormView.as_view(), name='formView'),
    url(r'^getforms/$', views.form_list, name='form_list'),
    url(r'^get_form/?', views.FromListView.as_view(), )
]

urlpatterns = format_suffix_patterns(urlpatterns)