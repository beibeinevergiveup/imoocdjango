import os
import django
import smtplib
from email.mime.text import MIMEText
from imoocdjango import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imoocdjango.settings')
django.setup()


def send_mail():
    msg = MIMEText('贝贝 never give up', 'plain', 'utf-8')
    msg['FROM'] = "BEIBEI"
    msg['Subject'] = "beibei biubiu"
    receivers = ['tttbd@qq.com', '1137720412@qq.com']
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, )
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())

    server.close()
    pass


if __name__ == '__main__':
    send_mail()
