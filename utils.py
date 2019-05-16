#coding:gbk

import threading
import time

class FuncThread(threading.Thread):
    
    def __init__(self, func, *args, **kwargs):
        super(FuncThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.finished = False
        self.result = None

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)
        self.finished = True

    def is_finished(self):
        return self.finished

    def get_result(self):
        return self.result


# def sleep(n):
#     time.sleep(n)
#     print('sleep %s second' % n)
#     return 'money'
#
#
# def do_in_thread(func, *args, **kwargs):
#     ft = FuncThread(func, *args, **kwargs)
#     ft.start()
#     return ft
#
# t = do_in_thread(sleep, 2)
# time.sleep(2.5)
# print(t.get_result())