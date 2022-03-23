import copy


class Monom:
    def __init__(self, power, coef=1):
        self.power = power
        self.coef = coef
        self.next = None

    def __mul__( self, other ):  # mul function
        if type(self) == Monom and (type(other) == int or type(other) == float):  # get monom and scalar
            return Monom(self.power, self.coef * other)

        if type(self) == type(other):  # get two monoms
            return Monom(self.power + other.power, self.coef * other.coef)

    def __rmul__( self, other ):  # get scalar and monom (right side)
        return Monom(self.power, self.coef * other)

    def __repr__( self ):
        if self.power == 1 and self.coef != 0:  # display option 1
            if type(self.coef) == int and self.coef != 1:
                if self.coef != 1 and self.coef > 0:
                    return str(self.coef) + "X"
                return "(" + str(self.coef) + "X)"
            if self.coef == 1:
                return "X"
            if self.coef % 1 != 0:
                if self.coef < 0:
                    return "(" + str(self.coef) + 'X)'
                return str(self.coef)+"X"
            return helper_with_float(str(self.coef)) + "X"

        if self.power == 0:  # display option 2
            if self.coef == 1:
                return str(1)

            if self.coef >= 0:  # display option 3
                return str(self.coef)
            if self.coef % 1 == 0:
                return "(" + str(self.coef) + ")"
            if self.coef % 1 != 0:
                x = round(self.coef, 2)
                return "(" + str(x) + ")"

        if self.coef == 1:  # display option 4
            return 'X^' + str(self.power)

        if self.coef % 1 == 0 and type(self.coef) == float and self.coef != 0:  # display option 5
            if self.coef >= 0:
                return helper_with_float(str(self.coef)) + "X^" + str(self.power)
            x = helper_with_float(str(self.coef)) + "X^" + str(self.power)
            return "(" + x + ")"

        if self.coef % 1 != 0 and self.coef > 0:  # display option 6
            x = round(self.coef, 2)
            if x % 1 == 0:
                return str(int(x)) + 'X^' + str(self.power)
            return str(x) + 'X^' + str(self.power)

        if self.coef == 0:  # display option 7
            return str(0)

        if self.coef < 0:  # display option 8
            x = round(self.coef, 2)
            return '(' + str(x) + 'X^' + str(self.power) + ')'
        return str(self.coef) + 'X^' + str(self.power)

    def derivative( self ):  # return the monom derivative
        return Monom(self.power - 1, self.coef * self.power)

    def integral( self ):  # return the monom integral
        if self.coef == 0:
            return 0
        if self.power == 0 and self.coef == 1:
            return Monom(1, 1)
        new_power = self.power + 1
        return Monom(self.power + 1, self.coef / new_power)


def helper_with_float( string ):  # helper find the number without the point
    new_coef = ""
    for i in string:
        if i != '.':
            new_coef += i
        else:
            return new_coef


def find_the_big_number( dict1, dict2 ):
    if len(dict1) == 0:
        return False
    if len(dict2) == 0:
        return True
    len_number = (max(len(dict1), len(dict2)))
    for i in range(len_number):
        if (list(dict1.keys())[i]) == (list(dict2.keys())[i]):  # same power
            if (list(dict1.values())[i]) > (list(dict2.values())[i]):  # different coef
                return False
            if (list(dict1.values())[i]) < (list(dict2.values())[i]):  #
                return True
        if (list(dict1.keys())[i]) != (list(dict2.keys())[i]):  # different power
            if (list(dict1.keys())[i]) > (list(dict2.keys())[i]):  #
                return False
            if (list(dict1.keys())[i]) < (list(dict2.keys())[i]):  #
                return True
    return False


def minus_dict_to_one( dict1, dict2, max_rank ):  # take two dict and return new list after minus them
    new_list = []
    for i in range(1, max_rank + 1):
        if i in dict1.keys() or i in dict2.keys():
            if i not in dict1.keys():
                dict1[i] = 0
            if i not in dict2.keys():
                dict2[i] = 0
            new_list.append((i, dict1[i] - dict2[i]))
    return new_list


class Polynomial:
    def __init__(self, l):
        if not isinstance(l, list):
            raise ValueError('Invalid polynomial initialization.')
        for i in l:
            if not isinstance(i, tuple) or len(i) != 2:
                raise ValueError('Invalid polynomial initialization.')
        for i in l:
            for j in i:
                if isinstance(j, int) or isinstance(j, float):
                    continue
                else:
                    raise ValueError('Invalid polynomial initialization.')
        self.l = l
        self.head = None

        for i in self.l:  # add them to the list
            self.add_at_starts(i)

    def add_at_starts( self, value ):  # add monom to the list
        new_monom = Monom(value[0], value[1])
        if self.head is None:
            self.head = new_monom
        else:
            tmp = self.head
            self.head = new_monom
            self.head.next = tmp

    def calculate_value( self, val ):  # get number and return the value
        x = self.head
        sum_value = 0
        while x is not None:
            sum_value += (val ** x.power) * x.coef
            x = x.next
        return int(sum_value)

    def rank( self ):  # find the poly rank
        full_poly, dict_power_coef = self.sorted_the_poly()
        if len(dict_power_coef) != 0:
            for i in dict_power_coef.keys():
                if i is not None:  # if it's not empty poly
                    return i
        return int(0)

    def plus_the_same_power( self ):  # get a tuple list and plus the same power
        dict_monom, updating_tuple = {}, []
        x = self.head
        while x is not None:  # while the link list not empty
            if x.power not in dict_monom:  # new_power
                dict_monom[x.power] = x.coef
            else:  # the same power
                dict_monom[x.power] += x.coef
            x = x.next

        for i in sorted(dict_monom.keys(), reverse=True):
            updating_tuple.append((i, dict_monom[i]))
        return updating_tuple

    def sorted_the_poly( self ):  # return the poly (without twice same power) and his dict (power : coef)
        full_poly, dict_power_coef = "", {}
        x = self.plus_the_same_power()  # mix the same power monom
        for i in x:
            if i[1] != 0:
                full_poly += str(Monom(i[0], i[1])) + "+"
                dict_power_coef[i[0]] = i[1]

        full_poly = full_poly[:-1]
        return full_poly, dict_power_coef

    def __neg__( self ):  # negative all the poly
        neg_poly = []
        for i in self.l:
            neg_poly.append((i[0], -i[1]))
        neg_poly = Polynomial(neg_poly)
        return neg_poly

    def __eq__( self, other ):  # check if the poly are the same
        tuple_first = Polynomial(self.l)
        tuple_second = Polynomial(other.l)
        return str(tuple_first) == str(tuple_second)

    def __ge__( self, other ):  # self > other / self == other
        if len(self.l) == 0 and len(other.l) > 0:
            return False
        if len(self.l) > 0 and len(other.l) == 0:
            return True
        if self == other or self > other:
            return True
        return False

    def __lt__( self, other ):  # self < other
        full_poly, dict_power_coef = self.sorted_the_poly()
        full_poly_other, dict_power_coef_other = other.sorted_the_poly()

        if self.rank() < other.rank():
            return True
        if self.rank() > other.rank():
            return False

        return find_the_big_number(dict_power_coef, dict_power_coef_other)

    def __add__( self, other ):  # add polynomials
        return Polynomial(self.l + other.l)

    def __sub__( self, other ):  # return the sub polynomials
        full_poly, dict_power_coef = self.sorted_the_poly()
        full_poly_other, dict_power_coef_other = other.sorted_the_poly()
        max_rank = max(self.rank(), other.rank())
        x = minus_dict_to_one(dict_power_coef, dict_power_coef_other, max_rank)
        return Polynomial(x)

    def __mul__( self, other ):
        new_poly = []
        full_poly, dict_power_coef = self.sorted_the_poly()
        if type(other) == int or type(other) == float:  # Part A : get scalar and return poly after scalar mul
            for i in dict_power_coef.keys():
                new_poly.append((i, dict_power_coef[i] * other))
            return Polynomial(new_poly)
        else:  # Part B : get two poly and mul them
            full_poly_other, dict_power_coef_other = other.sorted_the_poly()
            poly_mul = []
            for j in other.l:
                for i in self.l:
                    res = (Monom(j[0], j[1]) * Monom(i[0], i[1]))  # just power
                    poly_mul.append((res.power, res.coef))  # get the tuples result
            return Polynomial(poly_mul)

    def __rmul__( self, other ):  # get a scalar (on the left side) and return the poly after scalar mul
        new_poly = []
        full_poly, dict_power_coef = self.sorted_the_poly()
        for i in dict_power_coef.keys():
            new_poly.append((i, dict_power_coef[i] * other))
        return Polynomial(new_poly)

    def derivative( self ):  # return the polynomial derivative
        derivative_poly = []
        for i in self.l:
            derivative_poly.append((i[0] - 1, i[0] * i[1]))
        return Polynomial(derivative_poly)

    def integral( self, other=0 ):  # return the polynomial integral
        derivative_poly = []
        for i in self.l:
            derivative_poly.append((i[0] + 1, i[1] / float(i[0] + 1)))
        if other != 0:
            derivative_poly.append((0, other))
        return Polynomial(derivative_poly)

    def __repr__( self ):
        full_poly, dict_power_coef = self.sorted_the_poly()
        if full_poly == "":
            full_poly = str(0)
        return "P(X)=" + full_poly


class BinTreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None

    def __repr__( self ):
        return str(self.value)


class PolynomialBST:
    def __init__(self):
        self.head = None

    def insert( self, val ):  # sorting the value by binary rules

        def insert_rec( node, val ):

            if val <= node.value:  # left side
                if node.left is None:  # the leaf is empty
                    node.left = BinTreeNode(val)
                else:  # the leaf exists
                    insert_rec(node.left, val)

            else:  # right side
                if node.right is None:  # the leaf is empty
                    node.right = BinTreeNode(val)
                else:  # the leaf exists
                    insert_rec(node.right, val)

        if self.head is None:  # empty tree
            self.head = BinTreeNode(val)  # creating the root
        else:
            insert_rec(self.head, val)

    def in_order( self ):  # return the sorting value in the tree (left to right)
        def in_order_rec( root_tree, sorted_list ):
            if root_tree is not None:
                in_order_rec(root_tree.left, sorted_list)
                sorted_list.append(root_tree.value)
                in_order_rec(root_tree.right, sorted_list)
                return sorted_list

        if self.head is None:  # empty tree
            return '[]'
        else:
            return in_order_rec(self.head, [])

    def __add__( self, other ):  # add another tree to the first - return new binary tree
        tree = PolynomialBST()
        for i in self.in_order():
            tree.insert(i)
        for j in other.in_order():
            tree.insert(j)
        return tree
