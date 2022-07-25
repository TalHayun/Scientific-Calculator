# Scientific-Calculator

## Intro
In math, a polynomial of variable X is an Expression from the form: $a_{1} + a_{2}*x^2 + ... + a_{n}*x^n$ when $a_{1}, a_{2} + ..., a_{n}$ are constant .

The literals $a_{k}x^k$ are called **monomos**.
In this monom the power is k and the coefficient is $a_{k}$.

# Contents

- [Part A - Monom](#part-a-Monom)
- [Part B - Polynomial](#Part-B-Polynomial)
- [Part C - BinTreeNode](#Part-C-BinTreeNode)

## Part A - Monom

The Monom class will be a class containing the following fields:
  - power - the monom's power that represented by natural number
  - coef - the monom's coefficient that represented by real number
  - next - point to the next monomial link

The class will contain the following methods:
  - A constructor that accepts as parameters the power and the coefficient (default of the coefficient is 1)
  - `__repr__` opperation which returns a string representing the monomial by math format (eg: monom that contain power 6 and coefficient 3 will returned - $3x^6$)
    
    Important Rules: 
    - A power equal to 1 will not be printed ($x^1$ -> x)
    - A power equal to 0 will not be printed
    - A power equal to 1 will not be printed ($1*x$ -> x)
    - A coefficient that the value after the point is 0, will be printed as an integer
    - A coefficient that the value after the point is not 0, will be printed as round 2 digits after the point
    - A cofficient equal to 0 will be printed 0
    - A negative cofficient will be printed with parenthesis
    
  - `derivative` method that does not receive parameters in the call. When the method is activated, a new monomial object will be returned with the derived value of the monomial on which the function was applied ((a*$x^{n}$)' = n*$ax^{n-1}$)
  
  - `integral` method that does not receive parameters in the call. When the method is activated, a new monomial object will be returned with the integral value of the monomial on which the function was applied $\left(\int x^{n} \ dx = \frac{x^{n+1}}{n+1} \right)$
  
  
