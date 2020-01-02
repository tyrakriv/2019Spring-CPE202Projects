#This function determines if it is possible to win the bear game by starting with n bears.
#If it is deemed impossible, the function will return false.
def bears(n):
    #tests if the length of n is greater than 1 to determine product of last two digits
    if len(str(n)) > 1:
        n = str(n)
        pro = int(n[-1])*int(n[-2])
        n = int(n)

    #tests if 42 is n to return true statement
    if n == 42:
        return True

    #returns false if the number is less than 42
    if n < 42:
        return False

    #determines if n is divisible by 2 and if bears(n//2) returns True
    if n%2 == 0 and bears(n//2):
        return True

    #determines if n is divisible by 3 or 4 and if the product of the last two digits are not 0 and if bears(n-pro) returns True
    if (n%3 == 0 or n%4 == 0) and pro != 0 and bears(n-pro):
        return True

    #determines if n is divisible by 5 and bears(n-42) is True
    if n%5==0 and bears(n-42):
        return True

    #if nothing works, returns False
    else:
        return False
