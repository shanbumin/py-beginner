
# 1*1=1
# 1*2=2  2*2=4
#...
# 1*9=9  2*9=18  ...     9*9=81

#i表示第几行
#j表示某行的列数
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()
