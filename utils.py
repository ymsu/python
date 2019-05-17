#coding:gbk

import threading
import time
import os

# 线程类

class FuncThread(threading.Thread):
    """
    自己定义的线程类
    """
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

    def do_in_thread(func, *args, **kwargs):
        ft = FuncThread(func, *args, **kwargs)
        ft.start()
        return ft

# 函数执行超时时间判断

def handle_timeout(func, timeout, *args, **kwargs):
    """
    在一段时间（超时时间 timeout）内检查某一件事情（函数）是否完成，
    如果完成，则拿到返回的结果并退出超时，如果没有完成，返回 False 或者 None, 代表这件事情在超时时间内没有完成 （timeout）
    """
    interval = 1
    
    ret = None
    while timeout > 0:
        begin_time = time.time()
        ret = func(*args, **kwargs)
        if ret:
            break
        time.sleep(interval)
        timeout -= time.time() - begin_time
    
    return ret
