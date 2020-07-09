import cmath
import math
from math import sqrt

def main():
    print()
    print('Welcome to Quadratic Equation Solver (x^2 + bBx +  = 0): ')
    print()

    # creating coefficients added by the user
    coef = []
    for i in range(1,4):
        numbers = float(input("Enter three numbers (one each time): "))
        coef.append(numbers)
    # print(coef)

    # associating each value to a coefficient
    a,b,c = coef[0],coef[1],coef[2]
    print()
    print('coefficient a: {} | coefficient b: {} | coefficient c: {:.2f}'.format(a,b,c))

    # discriminant
    d = (b**2) - (4*a*c)
    # print(d)

    # conditions
    if d > 0:
        quad_1 = (-b + math.sqrt(d))/2*a
        quad_2 = (-b - math.sqrt(d))/2*a
    elif d == 0:
        quad_1 = quad2 = -b/(2*a)
    else:
        quad_1 = (-b + cmath.sqrt(d))/2*a
        quad_2 = (-b - cmath.sqrt(d))/2*a

    print()
    print("Results of x1 is: {:.2f} and x2 is: {:.2f}".format(quad_1,quad_2))
    print()

if __name__ == '__main__':
    main()

