import random

count = 0
num = 1
num_list = []

for i in range(25):
    num_list.append(num)
    count = count + 1
    if count == 5:
        count = 0
        num = num + 1

print(num_list)
random.shuffle(num_list)
print(num_list)

with open('num1.txt','wt')as f:
    for x in num_list:
        f.write(str(x)+'\n')
