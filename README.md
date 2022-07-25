# Scientific-Calculator

## Intro
In math, a polynomial of variable X is an Expression from the form: $a_{1} + a_{2}*x^2 + ... + a_{n}*x^n$ when $a_{1}, a_{2} + ..., a_{n}$ are constant .

The literals $a_{k}x^k$ are called **monomos**.
In this monom the power is k and the coefficient is $a_{k}$.

# Contents
==========

<!--ts-->
- [Part A - Monom](#Part-A-Monom)
- [Part B - Polynomial](#Part-B-Polynomial)
- [Part C - BinTreeNode](#Part-C-BinTreeNode)
<!--te-->


Part A - Monom
=================

The monom class will be a class containing the following fields:
  - power - the monom's power that represented by natural number
  - coef - the monom's coefficient that represented by real number
  - next - point to the next monomial link

The class will contain the following methods:
  - A constructor that gets as parameters the power and the coefficient (default of the coefficient is 1)
  - `__repr__` opperation which returns a string representing the monomial by math format (eg: monom that contain power 6 and coefficient 3 will returned - $3x^6$)
    
    Important Rules: 
    - A power equal to 1 will not be printed ($x^1$ → x)
    - A power equal to 0 will not be printed
    - A power equal to 1 will not be printed ($1*x$ → x)
    - A coefficient that the value after the point is 0, will be printed as an integer
    - A coefficient that the value after the point is not 0, will be printed as round 2 digits after the point
    - A cofficient equal to 0 will be printed 0
    - A negative cofficient will be printed with parenthesis
    
  - `derivative` A method that does not receive parameters in the call. When the method is activated, a new monomial object will be returned with the derived value of the monomial on which the function was applied ((a*$x^{n}$)' = n*$ax^{n-1}$)
  
  - `integral` A method that does not receive parameters in the call. When the method is activated, a new monomial object will be returned with the integral value of the monomial on which the function was applied $\left(\int x^{n} \ dx = \frac{x^{n+1}}{n+1} \right)$
  
Part B - Polynomial
======================

The polynomial class will be a class that describe a polynomial in a linked list of monomials as described in the following figure:

<img src = "https://user-images.githubusercontent.com/87673883/180789121-3e993766-9eec-434c-a96e-b49df5fb85ce.png" height = "150" width = "500" >

The monom class will be a class containing the following field:
  - head - head of a linked list of links, the list will be sorted by powers in descending order

The class will contain the following methods:
  - `__init__` Gets as a parameter a list containing tuples of two numeric members each. Within the tuple, the first item is the power and the second is the coefficient of the monomial
    
    Incorrect input: 
    - The type's parameter isn't a list
    - At least one of the elements of the list is not of tuple type
    - At least one of the elements of the list is not of size 2
    - The tuple's items are not numerical
    
    Each incorrect input will be raised a valueError with a caption: `invalid polynomic initiation`.
    An empty list is considered normal, a monomial with a coefficient of 0 will not be added to the linked list of the monomials.
    
  - `__repr__` An opperation which returns a string representing the polynomial
  - `rank` method that does not receive parameters in the call. This method returns the highest power of the polynomial (for a polynomial without monomials the power will be 0)
  - `calculate_value` An operation that receives an X numeric value and returns the numerical value obtained from putting in a polynomial
  - `__neg__` A method that returns a new polynomial identical to the polynomial on which the operation was applied except for the sign of the coefficients. The coefficients' sign will be opposite to the polynomial on which the operation was applied
  - `__sub__` A method that returns a new polynomial that containing the polynomial subtraction operation received as a parameter in the polynomial on which the operation was applied
  - `__add__` A method that returns a new polynomial that containing the polynomial addition operation received as a parameter in the polynomial on which the operation was applied
  - `__mul__` An opperation that gets a scalar or polynomial, the multiplication operation is defined as:
    -  multiplication polynomial in a scalar - returns a new polynomial in which all the coefficients are the coefficients of the original polynomial multiplied by the scalar
    -  multiplication polynomial in a polynomial - returns a new polynomial which is an addition multiplying each monomial from one of the polynomials in the other polynomial
    - `derivative` A method that returns a new polynomial containing a list of which each items is the derivative of a monomial of the list in the original polynomial
    - `integral` A method will return a new polynomial containing a list in which each items is the integral of a monomial of the list in the original polynomial
    
 In addition, all six comparison operations are supported: `=`,`≠`, `<`, `>`, `≤`, `≥`.
 
Part C - BinTreeNode
=======================

The class will contain the following field:
  - head - head of a tree, in an empty tree contain None or points to the first Node that was inserted to the tree.
  The nodes will be without key, the comparison will be according to the different comparison operations for each polynomial.
  
The class will contain the following methods:
  - `insert` A method that gets an sorted polynomial. The insertion of a term containing a polynomia less than or equal to a term containing an existing polynomial will be in the left child of the term of the existing polynomial (greather polynomial will be in the right child)
  - `in_order` A method that return the polynomial's list in the tree.
  - `__add__` A opperation that gets an two binary trees and returns a new binary tree containing both sides of the trees.






