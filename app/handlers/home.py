#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join
import requests

import tornado
from send_mail import Mail


class HomeHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        kwargs = {
            "mensagem": None
        }
        self.render('home.html', **kwargs)


class EnviandoEmailHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        self.set_status(200)
        dados_do_email = {
            "de": self.get_argument("de", "telecomaster@gmail.com"),
            "para": self.get_argument("para", "cyber.apt@bol.com.br"),
            "porta": int(self.get_argument("porta", 587)),
            "corpo": self.get_argument("corpo", "E-mail da fase 1"),
            "anexo": self.get_argument("anexo", None),
        }
        mail = Mail(dados_do_email["de"], dados_do_email["para"])
        mail.send(dados_do_email["corpo"], dados_do_email["porta"], dados_do_email['anexo'])
        self.finish()


class EnvioDeEmailHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def post(self):
        dados_do_email = {
            "de": self.get_argument("de", "telecomaster@gmail.com"),
            "para": self.get_argument("para", "cyber.apt@bol.com.br"),
            "porta": self.get_argument("porta", "587"),
            "corpo": self.get_argument("corpo", "E-mail da fase 1"),
        }
        if "anexo" in self.request.files:
            anexo = self.request.files['anexo'][0]
            nome_do_arquivo = join(self.application.settings["media_path"], anexo['filename'])
            arquivo = open(nome_do_arquivo, 'wb')
            arquivo.write(anexo['body'])
            arquivo.close()
            dados_do_email["anexo"] = nome_do_arquivo

        mensagem_retorno = "Erro no envio de e-mail. Tente de novo, por favor."
        status = "error"
        try:
            mail_response = requests.post("http://localhost:8001/envia-email/", dados_do_email)
            if mail_response.status_code == 200:
                mensagem_retorno = "E-mail enviado. Verifique a ferramenta de monitoração"
                status = "success"
        except requests.exceptions.ConnectionError:
            mensagem_retorno = "Serviço de e-mail não encontrado."
            status = "error"

        kwargs = {
            "mensagem": mensagem_retorno,
            "status": status,
        }
        self.render('home.html', **kwargs)
