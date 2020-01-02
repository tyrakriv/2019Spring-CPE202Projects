#This function will generate permutations of a string in lexicographic order.

def perm_gen_lex(a):
    #makes an empty, new list
    perm_list = []

    #tests if string contains no characters
    if a == '':
        return []

    #tests if string only contains one character and returns character
    if len(a) == 1:
        return [a]

    #goes through every character in the string
    for i in range(len(a)):
        
        #creates a shorter string without a character
        simple = a.replace(a[i],"")

        #calls function again to shorten the string until one character is left
        short = perm_gen_lex(simple)

        #for every character the first for loop goes through, the second will append
        #the new string into the perm_list to store
        for j in short:
            perm_list.append(a[i] + j)

    #perm_list is returned at the very end of the function
    return (perm_list)
