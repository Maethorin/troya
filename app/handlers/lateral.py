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
            output = sh.rdesktop("172.20.10.13", u="Administrador", p="Troca123", a="16", _bg=True)
            if output.exit_code != 0:
                mensagem = "Ocorreu um erro na execução do rdesktop e retornou %s" % output.exit_code
                status = "error"
        except sh.ErrorReturnCode, ex:
            mensagem = "Ocorreu um erro na execução: %s" % ex.stderr
            status = "error"

        kwargs = {
            "mensagem": mensagem,
            "status": status,
            "page": "fase-lateral",
        }
        self.render('lateral.html', **kwargs)
