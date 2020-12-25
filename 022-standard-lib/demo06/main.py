

import hashlib
# 计算文件的MD5摘要
hasher = hashlib.md5()

with open('sbm.txt', 'rb') as file:
    data = file.read(512)
    while data:
        hasher.update(data)
        data = file.read(512)

print(hasher.hexdigest())


