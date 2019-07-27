import time
import random
import requests
import datetime

def test():
    while True:
        time.sleep(1)
        tick = time.time()
        #requests.get('http://127.0.0.1:8000/api/v1.0/service/test')
        requests.get('http://127.0.0.1:8000/api/v1.0/service/image/list')
        tock = time.time()
        print('send request at %s, request cost: %.4f' % (str(datetime.datetime.now()), tock - tick))


if __name__ == '__main__':
    test()
