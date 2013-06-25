#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado


class HomeHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        kwargs = {
            "mensagem": None,
            "page": "home",
        }
        self.render('home.html', **kwargs)
