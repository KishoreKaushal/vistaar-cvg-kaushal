#!/usr/bin/python3

n  = int(input())

sum = 0.0

for i in range(n):
    sum+=float((i+1)/(i+2))

print("%.2f" % round(sum,2))
