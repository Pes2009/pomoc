from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from qucikstart import views

urlpatterns = [

    url(r'^ziom/$', views.ZiomList.as_view()),
    url(r'^ziom/(?P<pk>[0-9]+)/$', views.ZiomDetail.as_view()),
    url(r'^ziomka/$', views.ZiomkaList.as_view()),
    url(r'^ziomka/(?P<pk>[0-9]+)/$', views.ZiomkaDetail.as_view()),
    url(r'^words/$', views.WordsList.as_view()),
    url(r'^words/(?P<pk>[0-9]+)/$', views.WordsDetail.as_view()),
    url(r'^categories/$', views.CategoriesList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoriesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
