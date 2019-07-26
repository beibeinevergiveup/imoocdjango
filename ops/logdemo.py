import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imoocdjango.settings')
django.setup()


def logdemo():
    logger = logging.getLogger('django')
    logger.info('hello logging')
    logger.debug('hello debug log')
    logger.info('hello.filter logging')


if __name__ == '__main__':
    logdemo()
