from typing import Dict

memo:Dict[int,int] = {0:0,1:1}

def fib(n):
    return fib(n-2) + fib(n-1)

def fib2(n:int) -> int:
    print("fib2({})".format(n))
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]

if __name__ == "__main__":
    #fib(3)
    print(fib2(5))
    print(fib3(5))