import os


# 遍历文件夹下的文件
def tree_dir(dir_path,n=0) :
    global tree_str
    if os.path.isfile(dir_path):
        tree_str += '    |' * n + '—' * 4 + os.path.basename(dir_path) + '\n'
    elif os.path.isdir(dir_path):
        tree_str += '    |' * n + '—' * 4 + os.path.basename(dir_path)  +'\n'
        for i in os.listdir(dir_path):
            #os.listdir(path) 返回path路径下的文件名以列表形式存储的字符串
            #os.path.abspath(file_name) 返回file_name 的绝对路径
            tree_dir(dir_path+"/"+i ,n+1)
  

if __name__ == "__main__" :
    tree_str = ''
    dir_path = "/张衡杯接收发送nrf"
    tree_dir(dir_path)
    print(tree_str)
   #判断路径是否为文件
   # os.path.isfile(path)
   # # 判断路径是否为目录
   # os.path.isdir(path)
   # # 返回文件名
   # os.path.basename(path)
   # # 返回文件路径
   # os.path.dirname()
