#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cybersg'

from django.conf.urls import url, patterns
from api_manager import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^template/(?P<template>\w+)/$', views.template, name='template'),
    url(r'^api/$', views.api, name='new_api'),
    url(r'^api/(?P<api_id>\d+)/$', views.api, name='edit_api'),
    url(r'^api/(?P<api_id>\d+)/delete/$', views.delete_api, name='delete_api'),
    url(r'^queries/(?P<api_id>\d+)/$', views.queries, name='queries'),
    url(r'^query/(?P<api_id>\d+)/$', views.query, name='new_query'),
    url(r'^query/(?P<api_id>\d+)/(?P<query_id>\d+)/$', views.query, name='edit_query'),
    url(r'^query/(?P<query_id>\d+)/delete/', views.delete_query, name='delete_query')
)