def two_positive_digits(num1, num2, num3):
    if num1 > 0 and num2 > 0 and num3 < 0 :
        response = True
        return response
    elif num1 > 0 and num2 < 0 and num3 > 0:
        response = True
        return response
    elif num1 < 0 and num2 > 0 and num3 > 0:
        response = True
        return response
    
    
    else :
        response = False
        return False
    
print(two_positive_digits(2,-2,3))


