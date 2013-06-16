import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders


class Mail():
    def __init__(self, from_address, to_address):
        self.msg = MIMEMultipart('form-data')
        self.msg['Subject'] = "Fase 1 E-Mail"
        self.msg['From'] = from_address
        self.msg['To'] = to_address

    def send(self, body, port, attach):
        body = MIMEText(body, 'plain')
        self.msg.attach(body)
        if attach:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(attach, "rb").read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
            self.msg.attach(part)
        mail_server = smtplib.SMTP('relay.jangosmtp.net', port)
        mail_server.login("JohnSec", "761018WY")
        mail_server.sendmail(self.msg["From"], self.msg["To"], self.msg.as_string())
