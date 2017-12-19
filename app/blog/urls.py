# -*- coding: utf-8 -*-

from django.conf.urls import url
from app.blog import views

urlpatterns = [
    url(r'^tag$', views.tag, name='admin_tag'),
    url(r'^category$', views.category, name='admin_category'),
    url(r'^tag/ajax$', views.ajax_tag, name='admin_tag_ajax'),
    url(r'^category/ajax$', views.ajax_category, name='admin_category_ajax'),

    url(r'^article$', views.article, name='admin_article'),
    url(r'^article/ajax$', views.ajax_article, name='admin_article_ajax'),
    url(r'^article/add/$', views.article_add, name='article_add'),
    url(r'^article/(?P<article_id>\d+)/$', views.article_modify, name='article_modify'),

    url(r'^comment$', views.comment, name='admin_comment'),
    url(r'^comment/ajax$', views.ajax_comment, name='admin_comment_ajax'),
    url(r'^suggest$', views.suggest, name='admin_suggest'),
    url(r'^suggest/ajax$', views.ajax_suggest, name='admin_suggest_ajax'),
]