#Sum of all even numbers in fibonacci sequence below 4000000


def fib(maxnum):
    x,y=0,1
    while x<=maxnum:
        yield x
        x,y=y,x+y

total=sum(x for x in fib(4000000) if x%2==0) 

print(total)

