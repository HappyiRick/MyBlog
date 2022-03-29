import base64
import sys

fileName = sys.argv[1]
f=open(fileName,'rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)

bs=ls_f # 太长了省略
print("\n")
print(bs)
imgdata=base64.b64decode(bs)
file=open(fileName,'wb')
file.write(imgdata)
file.close()