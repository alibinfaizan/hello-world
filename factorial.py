
def factorial(n):
    fact = 1
    if n < 0:
        print('Negative values do not have factorials.')
    else:
        for i in range(1, n+1):
            fact *= i
        print(fact)
