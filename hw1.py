from operator import add, sub
def a_plus_b(a,b):
	"""Return a+abs(b),but without calling abs.
	>>> a_plus_b(2,3)
	5
	>>>a_plus_b(2,-3)
	5
	"""
	if b < 0:
		sub(a,b)
	else:
		add(a,b)
x = a_plus_b(2,3)
x

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a + b*b + c*c - min(a,b,c)*min(a,b,c)



def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
    
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """ Return anything else except 1

    >>> with_if_function()
    3
    """
    return if_function(c(), t(), f())

def c():
        global x
        x = 1
        return False

def t():
        global x
        x = 3

def f():
        return x 



def hailstone(n):
    k = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        k += 1
    return k
