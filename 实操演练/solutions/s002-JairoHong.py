def fibonacci(n):

    """Return n.

    
Args:
        n: n 2X1 retangles

    
Returns:
        number of methods.
    """

# Put your code here.
    
#填充的情况只有两种，竖着摆或者两个横着摆在一起
#f(n)中，最后一列若是竖着摆，则有f(n-1)种情况
#f(n)中，最后一列若是两个横着摆在一起，则有f(n-2)种情况
#   n = 0 or 1 作为初始情况，需要赋予初值
    if n <= 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
    
pass

if __name__ == "__main__":

    assert 1 == fibonacci(0)

    assert 1 == fibonacci(1)

    assert 2 == fibonacci(2)

    assert 8 == fibonacci(5)

    assert 89 == fibonacci(10)

    assert 10946 == fibonacci(20)
