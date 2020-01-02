def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""       
    #determines if the remainder is between 10 or 15
    if num%b >= 10 and num%b <= 15:
        #determines if remainder is 10 and calls function again with added A string
        if num% b == 10:
            return str(convert(num//b, b)) + 'A'
        #determines if remainder is 11 and calls function again with added B string
        if num% b == 11:
            return str(convert(num//b, b)) + 'B'
        #determines if remainder is 12 and calls function again with added C string
        if num% b == 12:
            return str(convert(num//b, b)) + 'C'
        #determines if remainder is 13 and calls function again with added D string
        if num% b == 13:
            return str(convert(num//b, b)) + 'D'
        #determines if remainder is 14 and calls function again with added E string
        if num% b == 14:
            return str(convert(num//b, b)) + 'E'
        #determines if remainder is 15 and calls function again with added F string
        if num% b == 15:
            return str(convert(num//b, b)) + 'F'

    #determines if the remainder and quotient is zero and returns the remainder as a string
    if num // b == 0 and num % b == 0:
        return str(num % b)

    #calls function and translates into variable string
    string = str(convert(num//b, b)) + str(num%b)

    #if the first character of the string is zero, return the string without the first character
    if string[0] == '0':
        return string[1:]
    #but if the first character is not zero, return the entire string
    else:
        return string
