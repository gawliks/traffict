#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cybersg'

from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect


class ViewProcessor(object):
    def __init__(self, request, model=None, form=None, context={}):
        self.model_cls = model
        self.form_cls = form
        self.request=request
        self.context = context
        self.response = None

    def get_context(self, form=None, object_id=None, prefix=''):
        if form is None:
            obj = None
            if object_id:
                obj = get_object_or_404(self.model_cls, pk=object_id)
            form = self.form_cls(instance=obj)
        if prefix: prefix += '_'
        ctx = {
            prefix + 'form': form,
            prefix + 'id': object_id
        }
        if self.context:
            ctx.update(self.context)
        return ctx

    def render(self, template_name, context={}):
        if self.context:
            context.update(self.context)
        else:
            context = self.context
        return render(self.request, template_name, context)

    def save(self, object_id=None, redirect_to=('api_manager:index',),
             success_message=None
    ):
        if object_id:
            obj = get_object_or_404(self.model_cls, pk=object_id)
            form = self.form_cls(self.request.POST, instance=obj)
        else:
            form = self.form_cls(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, success_message)
            self.response = redirect(*redirect_to)
            return True
        self.response = form
        return False
