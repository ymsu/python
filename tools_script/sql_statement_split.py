#coding:utf-8

source_filename = r'D:\python_project\ycyz\test1.txt'
target_filename = r'D:\python_project\ycyz\test2.txt'
lines = 1000
line_cnt = 0

with open(source_filename, 'r') as f1:
    with open(target_filename, 'w') as f2:
        f2.write('begin;\n')
        while True:
            line = f1.readline() # 整行读取数据
            print(line)
            f2.write(line)
            line_cnt += 1
            
            if line_cnt % lines == 0:
                line_cnt = 0
                f2.write("commit;\n")
                f2.write("begin;\n")

            
            if not line:
                f2.write("commit;\n")  
                break
            
            
    
     
    
    