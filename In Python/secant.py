def secant_method(f, x0, x1, tolerance=1e-6, max_iter=100):
    
    iteration = 0
    
    while iteration < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Check if denominator is zero
        if (fx1 - fx0) == 0:
            print("Division by zero error!")
            return None
        
        # Secant formula
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        # Check for convergence
        if abs(x2 - x1) < tolerance:
            return x2
        
        # Update values for next iteration
        x0 = x1
        x1 = x2
        iteration += 1
    
    print("Maximum iterations reached without convergence!")
    return x1

# Example usage
if __name__ == "__main__":
    # Example function: f(x) = x^2 - 4
    f = lambda x: x**2 - 4
    
    x0 = 1.0  # First initial guess
    x1 = 3.0  # Second initial guess
    
    root = secant_method(f, x0, x1)
    
    if root is not None:
        print(f"Root found: {root:.6f}")
        print(f"f({root:.6f}) = {f(root):.6f}")