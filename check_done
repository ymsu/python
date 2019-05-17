#coding:gbk

import time
import os
import utils


def check_file_exist(file_name):
    return os.path.exists(file_name)

def handle_timeout(func, timeout, *args, **kwargs):
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

def dump_data():
    time.sleep(5)
    f = open(r'C:\Users\1\Desktop\finish', 'w')
    f.close()


utils.do_in_thread(dump_data)

"""在一分钟之内检查桌面上是否有finish这样一个文件，如果有，返回True，
   如果没有，继续检查，直到超时
"""
print(handle_timeout(check_file_exist, 3, r'C:\Users\1\Desktop\finish'))

