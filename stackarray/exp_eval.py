from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    input_str = input_str.split()
    stack = Stack(len(input_str))
    operators = ['-','+','/','*','**']
    for i in range(len(input_str)):

        if input_str[i] in operators:
            
            try:
                first = stack.pop()
                second = stack.pop()
            except IndexError:
                raise PostfixFormatException('Insufficient operands')           
            
            if input_str[i] == '+':
                ans = first+second
                stack.push(ans)
            elif input_str[i] == '-':
                ans = second-first
                stack.push(ans)
            elif input_str[i] == '*':
                ans = first*second
                stack.push(ans)
            elif input_str[i] == '/':
                if first == 0:
                    raise ValueError
                else:
                    ans = second/first
                    stack.push(float(ans))
            elif input_str[i] == '**':
                ans = second**first
                stack.push(ans)
                
        elif input_str[i] == '>>' or input_str[i] == '<<':
            first = (stack.pop())
            second = (stack.pop())

            if type(first) == float or type(second) == float:
                raise PostfixFormatException("Illegal bit shift operand")

            else:
                first = int(first)
                second = int(second)
                if input_str[i] == '>>':
                    ans = second >> first
                    stack.push(ans)
                else:
                    ans = second << first
                    stack.push(ans)

        else:
            try:
                if '.' in input_str[i]:
                    val = float(input_str[i])
                    stack.push(val)
                else:
                    val = int(input_str[i])
                    stack.push(val)
                
            except ValueError:
                raise PostfixFormatException('Invalid token')
            
    if stack.size() > 1:
        print('15')
        raise PostfixFormatException('Too many operands')

    else:
        print('16')
        return stack.pop()
    
def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """

    ex = []
    
    input_str = input_str.split()
    stack = Stack(len(input_str))

    operators = ['+','-','/','*','**','<<','>>']
    for i in range(len(input_str)):
        o1 = input_str[i]

        if o1 == ' ':
            o1 == o1
            
        if o1 == '(':
            stack.push(input_str[i])
        
        elif o1 == ')':
            notpar = True
            while notpar and stack.is_empty() == False:
                val = stack.pop()
                if val != '(':
                    ex.append(val)
                else:
                    notpar = False
        
        elif o1 in operators:
            
            is_op = True
            while stack.is_empty() == False and is_op:
                
                o2 = stack.pop()
                
                if o2 not in operators:
                    stack.push(o2)
                    is_op = False
                    
                else:
                        
                    if o2 == '>>' or o2 == '<<':
                        ex.append(o2)
                    elif (o2 == '**' or o2 == '/' or o2 == '*') and (o1 in ['*','/','+','-']):
                        ex.append(o2)
                    elif (o2 == '+' or o2 == '-') and (o1 in ['+','-']):
                        ex.append(o2)
                    else:
                        stack.push(o2)
                        is_op = False

            stack.push(o1)        

        else:
        
            ex.append(o1)

    end = []
    for i in range(stack.num_items):
        o = stack.pop()
        if o in operators:
            end.append(o)
    
    rpn = ' '.join(ex)
    end = ' '.join(end)
    return (rpn + ' ' + end).rstrip()

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""

    input_str = input_str.split()
    stack = Stack(len(input_str))
    operators = ['+','-','/','*','**','<<','>>']

    for i in range(len(input_str)):

        index = len(input_str)-1-i        
        val = input_str[index]
        
        if val in operators:

            op1 = stack.pop()
            op2 = stack.pop()
            string = op1 + ' ' + op2 + ' ' + input_str[index]

            stack.push(string)

        else:
            stack.push(input_str[index])

    return stack.pop()
            

