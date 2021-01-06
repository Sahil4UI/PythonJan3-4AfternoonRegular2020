Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #data types - int
>>> #Data types -> numbers - int,float(decimal),complex number(a+bi)
>>> a = 5
>>> b = 23
>>> a+b
28
>>> a-b
-18
>>> a/b
0.21739130434782608
>>> a*b
115
>>> #power
>>> 
>>> 2**5#** - power
32
>>> 22/7
3.142857142857143
>>> 22//7#//->floor divison
3
>>> 5/2
2.5
>>> 5//2
2
>>> #% - modulus - remainer
>>> 22%7
1
>>> 2%10
2
>>> 

>>> #module/library/package
>>> import math
>>> math.sqrt(5)#square root
2.23606797749979
>>> math.sqrt(49)
7.0
>>> math.floor(23.4356)
23
>>> math.ceil(23.23)
24
>>> math.ceil(23.0000000001)
24
>>> math.ceil(23.00)
23
>>> math.fabs(8)#float->absolute value
8.0
>>> math.fabs(-8)
8.0
>>> int(math.fabs(-8))
8
>>> int(math.fabs(-8.6))
8
>>> math.floor(math.fabs(-45.45))
45
>>> math.factorial(6)
720
>>> math.comb(3,2)
3

>>> math.perm(3,2)
6
>>> math.remainder(10,5)
0.0
>>> math.remainder(22,7)
1.0
>>> math.log10(10)
1.0
>>> math.log(1)
0.0
>>> math.radians(90)
1.5707963267948966
>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(*integers)
        Greatest Common Divisor.
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    lcm(*integers)
        Least Common Multiple.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    nextafter(x, y, /)
        Return the next floating-point value after x towards y.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.
    
    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> math.pi
3.141592653589793
>>> math.tau
6.283185307179586
>>> math.lcm(23,45,687)
237015
>>> math.gcd(34,76,24,18)
2
>>> math.gcd(100,200,300)
100
>>> x = 20.45
>>> y = 45.56
>>> x+y
66.01
>>> x-y
-25.110000000000003
>>> x*y
931.702
>>> x/y
0.4488586479367866
>>> x**2
418.2025
>>> #complex Numbers
>>> x= 1-5j
>>> type(x)
<class 'complex'>
>>> y=3-5j
>>> x
(1-5j)
>>> y
(3-5j)
>>> x+y
(4-10j)
>>> x-y
(-2+0j)
>>> x*y
(-22-20j)
>>> x/y
(0.8235294117647058-0.29411764705882354j)
>>> 28/34
0.8235294117647058
>>> 10/34
0.29411764705882354
>>> import math
>>> math.sqrt(x)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    math.sqrt(x)
TypeError: can't convert complex to float
>>> import cmath#complex math
>>> cmath.sqrt(x)
(1.7462845577958914-1.4316108957382214j)
>>> help(math)

>>> help(cmath)
Help on built-in module cmath:

NAME
    cmath

DESCRIPTION
    This module provides access to mathematical functions for complex
    numbers.

FUNCTIONS
    acos(z, /)
        Return the arc cosine of z.
    
    acosh(z, /)
        Return the inverse hyperbolic cosine of z.
    
    asin(z, /)
        Return the arc sine of z.
    
    asinh(z, /)
        Return the inverse hyperbolic sine of z.
    
    atan(z, /)
        Return the arc tangent of z.
    
    atanh(z, /)
        Return the inverse hyperbolic tangent of z.
    
    cos(z, /)
        Return the cosine of z.
    
    cosh(z, /)
        Return the hyperbolic cosine of z.
    
    exp(z, /)
        Return the exponential value e**z.
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two complex numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them must be
        smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
        not close to anything, even itself. inf and -inf are only close to themselves.
    
    isfinite(z, /)
        Return True if both the real and imaginary parts of z are finite, else False.
    
    isinf(z, /)
        Checks if the real or imaginary part of z is infinite.
    
    isnan(z, /)
        Checks if the real or imaginary part of z not a number (NaN).
    
    log(...)
        log(z[, base]) -> the logarithm of z to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of z.
    
    log10(z, /)
        Return the base-10 logarithm of z.
    
    phase(z, /)
        Return argument, also known as the phase angle, of a complex.
    
    polar(z, /)
        Convert a complex from rectangular coordinates to polar coordinates.
        
        r is the distance from 0 and phi the phase angle.
    
    rect(r, phi, /)
        Convert from polar coordinates to rectangular coordinates.
    
    sin(z, /)
        Return the sine of z.
    
    sinh(z, /)
        Return the hyperbolic sine of z.
    
    sqrt(z, /)
        Return the square root of z.
    
    tan(z, /)
        Return the tangent of z.
    
    tanh(z, /)
        Return the hyperbolic tangent of z.

DATA
    e = 2.718281828459045
    inf = inf
    infj = infj
    nan = nan
    nanj = nanj
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> cmath.pi
3.141592653589793
>>> x
(1-5j)
>>> x.real
1.0
>>> x.img
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    x.img
AttributeError: 'complex' object has no attribute 'img'
>>> x.imag
-5.0
>>> #String - string is a collection of characters where character can be alphabetical,numerical or special
>>> # ' ' , "  " , """   """
>>> x = "Sahil"
>>> type(x)
<class 'str'>
>>> x = 'Ram'
>>> type(x)
<class 'str'>
>>> # '',"" -> single line/single para
>>> x = 'Python is an interpreted, high-level and general-purpose programming language. Pythons design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs an object-oriented approach aim to h'
>>> x = "Python is an interpreted, high-level and general-purpose programming language. Pythons design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs an object-oriented approach aim to h"
>>> x = '[Python is an interpreted, high-level and general-purpose programming language. Pythons design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]'
SyntaxError: EOL while scanning string literal
>>> x = '''Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]'''
>>> print(x)
Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]
>>> x = """Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]"""
>>> print(x)
Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]
>>> string = "python is a "high level" programming"
SyntaxError: invalid syntax
>>> string = 'python is a "high level" programming'
>>> string = "python is a 'high level' programming"
>>> print(string)
python is a 'high level' programming
>>> string = "python is a \"high level\" programming"#escape sequence-used to disable functionality
>>> print(string)
python is a "high level" programming
>>> string1 = "hello\nEveryone"
>>> print(string1)
hello
Everyone
>>> string1 = "hello\tEveryone"
>>> string1
'hello\tEveryone'
>>> print(x)
Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[27]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[28]
>>> print(string1)
hello	Everyone
>>> #Indexing
>>> x = "hello"
>>> x[0]
'h'
>>> x[1]
'e'
>>> x[2]
'l'
>>> x[3]
'l'
>>> x[100]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    x[100]
IndexError: string index out of range
>>> x[-1]
'o'
>>> x[-2]
'l'
>>> x
'hello'
>>> len(x)
5
>>> #Slicing
>>> x[0:6]
'hello'
>>> x = "hello everyone how are you?"
>>> x[0:6]
'hello '
>>> x[:6]
'hello '
>>> x[5:]
' everyone how are you?'
>>> x[:]
'hello everyone how are you?'
>>> 