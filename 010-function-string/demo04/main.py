import os
import  time

# todo 需要在终端演示额
content='王大仙修成之法'

while True:
    os.system('clear')
    print(content)
    time.sleep(0.2)#0.2s =200ms
    content=content[1:]+content[0]