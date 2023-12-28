n = 3

"""
subfactorial
!x = x!*(Sigma((-1)^k/k!|k=0:k=x))
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

def subfactorial(n):
    return factorial(n) * sum([((-1)**k/factorial(k)) for k in range(0,n+1)])

print(subfactorial(n))
