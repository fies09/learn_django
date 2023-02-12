#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/7 13:07
# @Author     : fany
# @Project    : PyCharm
# @File       : base_view.py
# @description:
from django import urls
from django.views import View


class BaseView(View):
    path_type = "path"
    url = None
    name = None

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(BaseView, cls).as_view()
        path = getattr(urls, cls.path_type)
        return path(cls.url, view, name=cls.name)