def exactly_two_positive(a, b, c):
    # Count the number of positive integers 
    count_positive = sum([1 for num in [a, b, c] if num > 0])
    
    # exactly two integers are positive
    if count_positive == 2:
        return True
    else:
        return False

# Test cases
print(exactly_two_positive(2, 4, -3))   
print(exactly_two_positive(-4, 6, 8))   
print(exactly_two_positive(4, -6, 9))   
print(exactly_two_positive(-4, 6, 0))  
print(exactly_two_positive(4, 6, 10))  
print(exactly_two_positive(-14, -3, -4)) 