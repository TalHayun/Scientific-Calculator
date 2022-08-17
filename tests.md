# TESTS


## TEST-1

```raku
p1 = Polynomial([(1, 2), (2, 1), (5, 6), (6, 5), (1, 2), (2, 1)])
p2 = Polynomial([])
p3 = Polynomial([(8, 0), (3, -5), (3, 5), (0, 18)])
print('p1-p3:')
print(p1)
print(p2)
print(p3)
```

###### OUTPUT:
```raku
p1-p3:
P(X)=5X^6+6X^5+2X^2+4X
P(X)=0
P(X)=18
```


## TEST-2

```raku
print(p1, ' rank:', str(p1.rank()), )
print(p2, ' rank:', str(p2.rank()))
print(p3, ' rank:', str(p3.rank()))
print(p1, ' value(x=0):', str(p1.calculate_value(0)))
print(p1, ' value(x=1):', str(p1.calculate_value(1)))
print(p1, ' value(x=2):', str(p1.calculate_value(2)))
```

##### OUTPUT:
```raku
P(X)=5X^6+6X^5+2X^2+4X  rank: 6
P(X)=0  rank: 0
P(X)=18  rank: 0
P(X)=5X^6+6X^5+2X^2+4X  value(x=0): 0
P(X)=5X^6+6X^5+2X^2+4X  value(x=1): 17
P(X)=5X^6+6X^5+2X^2+4X  value(x=2): 528
```

## TEST-3

```raku
p4 = Polynomial([(1, 1), (2, 2), (3, 3)])
p5 = Polynomial([(1, 4), (2, 5), (3, 6)])
p6 = Polynomial([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
p7 = Polynomial([(1, -1), (2, -2), (3, 3), (4, -4), (5, -5), (6, -6)])
print('p4-p7(v1)')
print('p4:', p4)
print('p5:', p5)
print('p6:', p6)
print('p7:', p7)
print(p6, '+', p7, '=', (p6+p7))
print(p4, '+', p5, '=', (p4+p5))
print('-(', p6, ')=', -p6)
print(p6, '-', p7, '=', (p6-p7))
```

##### OUTPUT:
```raku
p4-p7(v1)
p4: P(X)=3X^3+2X^2+X
p5: P(X)=6X^3+5X^2+4X
p6: P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X
p7: P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X)
P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X + P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X) = P(X)=6X^3
P(X)=3X^3+2X^2+X + P(X)=6X^3+5X^2+4X = P(X)=9X^3+7X^2+5X
-( P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X )= P(X)=(-6X^6)+(-5X^5)+(-4X^4)+(-3X^3)+(-2X^2)+(-1X)
P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X - P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X) = P(X)=12X^6+10X^5+8X^4+4X^2+2X
```


## TEST-4

```raku
print('p4-p5(v2)')
print('p4:', p4)
print('p5:', p5)
print(p4, '*', p5, '=', (p4*p5))
print(p4, '*', 5, '=', (p4*5))
print(5, '*', p4, '=', (5*p4))
```

##### OUTPUT:
```raku
p4-p5(v2)
p4: P(X)=3X^3+2X^2+X
p5: P(X)=6X^3+5X^2+4X
P(X)=3X^3+2X^2+X * P(X)=6X^3+5X^2+4X = P(X)=18X^6+27X^5+28X^4+13X^3+4X^2
P(X)=3X^3+2X^2+X * 5 = P(X)=15X^3+10X^2+5X
5 * P(X)=3X^3+2X^2+X = P(X)=15X^3+10X^2+5X
```

## TEST-5

```raku
print('p4-p5(v3)')
print('(', p4, ")'=", p4.derivative())
print('(', p5, ")'=", p5.derivative())
print('integral(', p4, ")=", p4.integral())
print('integral(', p5, ")=", p5.integral())
print('integral(', p5, ")-18=", p5.integral(-18))
print('integral((', p4, ")')=", p4.derivative().integral())
```

##### OUTPUT:
```raku
p4-p5(v3)
( P(X)=3X^3+2X^2+X )'= P(X)=9X^2+4X+1
( P(X)=6X^3+5X^2+4X )'= P(X)=18X^2+10X+4
integral( P(X)=3X^3+2X^2+X )= P(X)=0.75X^4+0.67X^3+0.5X^2
integral( P(X)=6X^3+5X^2+4X )= P(X)=1.5X^4+1.67X^3+2X^2
integral( P(X)=6X^3+5X^2+4X )-18= P(X)=1.5X^4+1.67X^3+2X^2+(-18)
integral(( P(X)=3X^3+2X^2+X )')= P(X)=3X^3+2X^2+X
```


## TEST-6

```raku
print('p8-p9')
p8 = Polynomial([(1, 4), (2, 5), (3, 6)])
p9 = Polynomial([(1, 4), (2, 5), (3, 6)])
p10 = Polynomial([(1, 4.1), (2, 5), (3, 6)])
p11 = Polynomial([(4, 5)])
print(p8, '==', p9, ':', str(p8 == p9))
print(p8, '<=', p9, ':', str(p8 <= p9))
print(p8, '>=', p9, ':', str(p8 >= p9))
print(p8, '<', p9, ':', str(p8 < p9))
print(p8, '>', p9, ':', str(p8 > p9))
print(p8, '!=', p9, ':', str(p8 != p9))
print('p9-p10')
print(p9, '==', p10, ':', str(p9 == p10))
print(p9, '<=', p10, ':', str(p9 <= p10))
print(p9, '>=', p10, ':', str(p9 >= p10))
print(p9, '<', p10, ':', str(p9 < p10))
print(p9, '>', p10, ':', str(p9 > p10))
print(p9, '!=', p10, ':', str(p9 != p10))
print('p9-p11')
print(p9, '==', p11, ':', str(p9 == p11))
print(p9, '<=', p11, ':', str(p9 <= p11))
print(p9, '>=', p11, ':', str(p9 >= p11))
print(p9, '<', p11, ':', str(p9 < p11))
print(p9, '>', p11, ':', str(p9 > p11))
print(p9, '!=', p11, ':', str(p9 != p11))
```

##### OUTPUT:
```raku
p8-p9
P(X)=6X^3+5X^2+4X == P(X)=6X^3+5X^2+4X : True
P(X)=6X^3+5X^2+4X <= P(X)=6X^3+5X^2+4X : True
P(X)=6X^3+5X^2+4X >= P(X)=6X^3+5X^2+4X : True
P(X)=6X^3+5X^2+4X < P(X)=6X^3+5X^2+4X : False
P(X)=6X^3+5X^2+4X > P(X)=6X^3+5X^2+4X : False
P(X)=6X^3+5X^2+4X != P(X)=6X^3+5X^2+4X : False
p9-p10
P(X)=6X^3+5X^2+4X == P(X)=6X^3+5X^2+4.1X : False
P(X)=6X^3+5X^2+4X <= P(X)=6X^3+5X^2+4.1X : True
P(X)=6X^3+5X^2+4X >= P(X)=6X^3+5X^2+4.1X : False
P(X)=6X^3+5X^2+4X < P(X)=6X^3+5X^2+4.1X : True
P(X)=6X^3+5X^2+4X > P(X)=6X^3+5X^2+4.1X : False
P(X)=6X^3+5X^2+4X != P(X)=6X^3+5X^2+4.1X : True
p9-p11
P(X)=6X^3+5X^2+4X == P(X)=5X^4 : False
P(X)=6X^3+5X^2+4X <= P(X)=5X^4 : True
P(X)=6X^3+5X^2+4X >= P(X)=5X^4 : False
P(X)=6X^3+5X^2+4X < P(X)=5X^4 : True
P(X)=6X^3+5X^2+4X > P(X)=5X^4 : False
P(X)=6X^3+5X^2+4X != P(X)=5X^4 : True
```

## TEST-7

```raku
print('t1')
t1 = PolynomialBST()
t1.insert(p1)
t1.insert(p2)
t1.insert(p3)
t1.insert(p4)
t1.insert(p5)
print(t1.in_order())
print('t2')
t2 = PolynomialBST()
print(t2.in_order())
t2.insert(p6)
t2.insert(p7)
t2.insert(p8)
t2.insert(p9)
t2.insert(p10)
t2.insert(p11)
print(t2.in_order())
print('t3')
t3 = t1 + t2
print(t3.in_order())
```

##### OUTPUT:
```raku
t1
[P(X)=0, P(X)=18, P(X)=3X^3+2X^2+X, P(X)=6X^3+5X^2+4X, P(X)=5X^6+6X^5+2X^2+4X]
t2
[]
[P(X)=6X^3+5X^2+4X, P(X)=6X^3+5X^2+4X, P(X)=6X^3+5X^2+4.1X, P(X)=5X^4, P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X), P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X]
t3
[P(X)=0, P(X)=18, P(X)=3X^3+2X^2+X, P(X)=6X^3+5X^2+4X, P(X)=6X^3+5X^2+4X, P(X)=6X^3+5X^2+4X, P(X)=6X^3+5X^2+4.1X, P(X)=5X^4, P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X), P(X)=5X^6+6X^5+2X^2+4X, P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X]
```





