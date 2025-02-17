#include <stdio.h>
#include <math.h>

// Function to calculate f(x)
float f(float x) {
    // Change this function according to your equation
    return x*x*x - 4*x - 9; 
}

int main() {
    float a, b, c, error;
    int iterations = 0;
    
    printf("Enter interval [a, b]: ");
    scanf("%f %f", &a, &b);
    
    printf("Enter desired error tolerance: ");
    scanf("%f", &error);
    
    // Check if there's a root in the interval
    if (f(a) * f(b) >= 0) {
        printf("No root exists in this interval\n");
        return 1;
    }
    
    // Bisection process
    do {
        c = (a + b) / 2;
        printf("Iteration %d: Root = %f\n", ++iterations, c);
        
        if (f(c) == 0.0)
            break;
        else if (f(c) * f(a) < 0)
            b = c;
        else
            a = c;
            
    } while (fabs(b - a) >= error);
    
    printf("\nThe root is: %f\n", c);
    printf("Number of iterations: %d\n", iterations);
    
    return 0;
}