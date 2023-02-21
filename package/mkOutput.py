from os import path,mkdir
from os.path import isdir

# 資料夾相關

def mkOutputDir(path:str):
    if not isdir(path+"\output"):
        print('建立資料夾')
        mkdir(path+"\output")
    else:
        # print("資料夾已存在")
        pass

    return path+'\output'

# OUTPUT_PATH = mkOutputDir(input('輸入輸出路徑:')) 
# OUTPUT_PATH = mkOutputDir(r"C:\Users\雷克斯\Desktop") 

# open(OUTPUT_PATH+"\TEST.doc","a+")