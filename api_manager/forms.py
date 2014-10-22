#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cybersg'

from django import forms
from api_manager import models


class ApiForm(forms.ModelForm):
    class Meta:
        model = models.Api


class QueryForm(forms.ModelForm):
    class Meta:
        model = models.Query