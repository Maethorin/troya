#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import abspath, join, dirname
import logging

import tornado.web
import tornado.wsgi
from tornado.web import url
from handlers.c_e_c_server import CeCServerHandler
from handlers.home import HomeHandler
from handlers.email import EnvioDeEmailHandler, EnviandoEmailHandler


def configure_app(self, config=None, log_level='INFO', debug=False, static_path=None):
    if static_path is None:
        static_path = abspath(join(dirname(__file__), 'static'))
    template_path = abspath(join(dirname(__file__), 'templates'))
    media_path = abspath(join(dirname(__file__), 'media/'))

    self.config = config

    handlers = [
        url(r'/', HomeHandler, name="home"),
        url(r'/fase-email/?', EnvioDeEmailHandler, name="envia-email"),
        url(r'/envia-email/?', EnviandoEmailHandler, name="enviando-email"),

        url(r'/fase-c-e-c/?', CeCServerHandler, name="c-e-c-server"),
    ]

    options = {
        "cookie_secret": self.config.COOKIE_SECRET,
        "static_path": static_path,
        "static_url_prefix": self.config.STATIC_URL,
        "template_path": template_path,
        "media_path": media_path
    }

    if debug:
        options['debug'] = True
        config.NUMBER_OF_FORKS = 1

    return handlers, options


class App(tornado.web.Application):

    def __init__(self, config=None, log_level='INFO', debug=False, static_path=None):
        handlers, options = configure_app(self, config, log_level, debug, static_path)
        super(App, self).__init__(handlers, **options)
