"""
A module with a square function. Third test should fail.
"""

def square(x):
    """Squares x.

    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(0)
    1
    """

    return x * x

#
# Unit tests
#

def test_square_of_3_is_9():
    """Test that 3**2 = 9"""
    assert func(3) == 9

# 
# Main
# 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
