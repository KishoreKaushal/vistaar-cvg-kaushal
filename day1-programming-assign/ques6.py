#!/usr/bin/python3

result = []

def checkAllEven(x):
    while(True):
        if (x==0):
            return True
        if(x%2==0):
            x = x//10
        elif(x%2!=0):
            return False

for i in range(1000,3001):
    if checkAllEven(i):
        result.append(i)
    else:
        continue

ans=''
for num in result:
    ans+=str(str(num)+',')

print(ans[:-1])
