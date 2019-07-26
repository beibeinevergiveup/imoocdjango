# -*- encoding=utf-8 -*-


import os
import time
import django
import random
import hashlib

from backend import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from authorization.models import User


def ranstr(length):
    CHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(length):
        salt += random.choice(CHS)
    return salt

class DataTool:

    @classmethod
    def generate_fake_user_data(cls, count):
        new_user_list = []
        for i in range(count):
            open_id = ranstr(32)
            nickname = ranstr(10)
            new_user = User(open_id=open_id, nickname=nickname)
            new_user_list.append(new_user)
            if i % 10000 == 0:
                print('created %d items.' % i)
                User.objects.bulk_create(new_user_list)
                new_user_list = []
        pass


class TestTool:

    @classmethod
    def test_index(cls):
        test_nickname_list = []
        TEST_TIME = 10000
        for i in range(TEST_TIME):
            random_nickname = ranstr(32)
            test_nickname_list.append(random_nickname)
        # 计算时间
        begin = time.time()
        for nickname in test_nickname_list:
            user = User.objects.filter(nickname='mNQuuPKWzx')
        end = time.time()
        print('begin: %.6f, end: %.6f, cost: %.6f' %(begin, end, (end-begin)))


if __name__ == '__main__':
    DataTool.generate_fake_user_data(100000)
    TestTool.test_index()