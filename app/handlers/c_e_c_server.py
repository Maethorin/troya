#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tornado


class CeCServerHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        primeiro_get = "Primeira URL acessada com sucesso. Verifique a ferramenta de monitoração"
        primeiro_status = "success"
        primeira_url = "http://87.237.209.166/"
        try:
            response = requests.get(primeira_url)
            if response.status_code == 500:
                primeiro_get = "Erro ao tentar acessar a primeira URL."
                primeiro_status = "error"
            if response.status_code == 404:
                primeiro_get = "Primeira URL retornou não encontrado (404)"
                primeiro_status = "error"
        except requests.exceptions.ConnectionError:
            primeiro_get = "Erro ao tentar acessar a primeira URL."
            primeiro_status = "error"

        segundo_get = "Segunda URL acessada com sucesso. Verifique a ferramenta de monitoração"
        segundo_status = "success"
        segunda_url = "%sdl.php?file=PI232" % primeira_url
        try:
            response = requests.get(segunda_url)
            if response.status_code == 500:
                segundo_get = "Erro ao tentar acessar a segunda URL."
                segundo_status = "error"
            if response.status_code == 404:
                segundo_get = "Segunda URL retornou não encontrado (404)"
                segundo_status = "error"
        except requests.exceptions.ConnectionError:
            segundo_get = "Erro ao tentar acessar a segunda URL."
            segundo_status = "error"

        kwargs = {
            "mensagem": True,
            "primeiro_get": primeiro_get,
            "segundo_get": segundo_get,
            "primeiro_status": primeiro_status,
            "segundo_status": segundo_status,
            "primeira_url": primeira_url,
            "segunda_url": segunda_url,
            "page": "fase-c-e-c",
        }
        self.render('c-e-c-server.html', **kwargs)
