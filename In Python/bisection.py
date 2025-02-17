def func(x):
    return x**3 - x**2 + 2

def bisection(a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b\n")
        return None
    
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = func(c)
        
        if abs(fc) < tol:  # Close enough to zero
            return c
            
        if func(a) * fc < 0:
            b = c
        else:
            a = c
            
        if (b - a) < tol:  # Interval is small enough
            return c
    
    return (a + b) / 2

# Driver code
a = -200
b = 300
tol = 0.0001  # Error tolerance
root = bisection(a, b, tol)

if root is not None:
    print(f"The value of root is: {root:.6f}")
