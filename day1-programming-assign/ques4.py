#!/usr/bin/python3

words  = input().split(',')
words.sort()

string=''
for wrd in words:
    string+=(wrd+',')

string = string[0:-1]
print(string)
