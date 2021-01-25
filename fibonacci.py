def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

nth = int(input('Enter a number : '))

if nth<=0:
    print('You typed a negtive integer.')
else:
    for i in range(nth+1):
        print(fibo(i))
