def fib(n):
    """
    Renvoie le n+1 terme de la suite de Fibonacci
    """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)