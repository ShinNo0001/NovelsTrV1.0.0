from django.conf.urls import url
from .views import *

app_name="novel"

urlpatterns = [
    url(r'^novel-list/$', novel_list,name='novel-list'),
    url(r'^novel-create/$', novel_create,name='novel-create'),

    url(r'^Haberler/$', haberler,name='haberler'),
    url(r'^Haber-create/$', haber_create, name='haber-create'),
    url(r'^(?P<id>\d+)/haberler/$', haberler_detail, name='haberler-detail'),

    url(r'^chapter-create/$', chapter_create, name='chapter-create'),

    url(r'^(?P<slug>[\w-]+)/Novel_Detayı/$', chapter_detail, name='chapter_detail'),
    url(r'^(?P<slug>[\w-]+)/$', novel_detail, name='novel-detail'),

    url(r'^(?P<id>\d+)/delete/$', comment_delete, name='commentdelete'),
    url(r'^(?P<id>\d+)/yorum-sil/$', ncomment_delete, name='ncommentdelete'),


]
