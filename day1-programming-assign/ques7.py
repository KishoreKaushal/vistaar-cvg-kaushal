#!/usr/bin/python3

bal = 0

while(True):
    dat = input().split(' ')
    if(len(dat)==2):
        c = str(dat[0])
        amt = int(dat[1])
    else:
        break
    if(c=='D'):
        bal+=amt
    elif(c=='W'):
        bal-=amt

print(bal)
