# uuid模块可以帮助我们生成全局唯一标识符（Universal Unique IDentity）。该模块提供了四个用于生成UUID的函数，分别是：

# uuid1()：由MAC地址、当前时间戳、随机数生成，可以保证全球范围内的唯一性。
# uuid3(namespace, name)：通过计算命名空间和名字的MD5哈希摘要（“指纹”）值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字会生成相同的UUID。
# uuid4()：由伪随机数生成UUID，有一定的重复概率，该概率可以计算出来。
# uuid5()：算法与uuid3相同，只不过哈希函数用SHA-1取代了MD5。

# 由于uuid4存在概率型重复，那么在真正需要全局唯一标识符的地方最好不用使用它。
# 在分布式环境下，uuid1是很好的选择，因为它能够保证生成ID的全局唯一性。
import uuid
import time
print(uuid.uuid1().hex)
print(uuid.uuid1().hex)
print(uuid.uuid1().hex)

