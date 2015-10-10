import random

rand1 = 0
rand2 = 0
count = 0

while True: 
    if(rand1 == 17 and rand2 == 38):
        break
    else:
        rand1 = random.randint(1,99)
        rand2 = random.randint(1,99)
        count +=1

print(count)

