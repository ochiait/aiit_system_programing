import time, random

sum=0

before = time.clock()
for i in range(1000000) :
        sum = sum + random.randint(1,100)
gaptime = time.clock() - before

print ( "gaptime:" , gaptime , flush = True)
