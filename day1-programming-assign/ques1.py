
#!/usr/bin/python3

n = int(input())

def factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n

fact = factorial(n)
print(fact)
