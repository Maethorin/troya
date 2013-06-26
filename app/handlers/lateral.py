#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sh
import tornado


class LateralHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        mensagem = "Comando executado com sucesso. Verifique a ferramenta de monitoração."
        status = "success"
        try:
            sh.apt_get("install", "rdesktop", y=True)
            sh.rdesktop("172.20.10.13", u="Administrador", p="Troca123", a="16", k="none")
        except Exception:
            pass
        kwargs = {
            "mensagem": mensagem,
            "status": status,
            "page": "fase-lateral",
        }
        self.render('lateral.html', **kwargs)
