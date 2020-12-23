import  random

#掷骰子6000次，统计每次命中的点数的次数


counters=[0]*6

for _ in range(6000):
    face=random.randint(1,6)
    counters[face-1]+=1


for face in range(1,7):
    print(f'{face}点出现了{counters[face-1]}次')