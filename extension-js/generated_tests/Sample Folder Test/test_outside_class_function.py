

# This is count DigitOne Function
# It counts the number of occurrences of the numerical digit, 1.
def outside_class_function(n):
    count = 0
    for i in range(1, n+1):
            num = str(i)
            for j in num:
                if int(j) == 1:
                    count += 1
    return count

def test_outside_class_function_1():
    assert outside_class_function(10) == 1

def test_outside_class_function_2():
    assert outside_class_function(100) == 1

def test_outside_class_function_3():
    assert outside_class_function(1000) == 1

def test_outside_class_function_4():
    assert outside_class_function(10000) == 1

def test_outside_class_function_5():
    assert outside_class_function(100000) == 1
