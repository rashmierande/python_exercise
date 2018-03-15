'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Some examples:
 ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Solution:
The Reverse Polish Notation (RPN) is also known as the postfix notation, because each
operator appears after its operands. For example, the infix notation “3 + 4” is expressed
as “3 4 +” in RPN.

Observe that every time we see an operator, we need to evaluate the last two operands.
Stack fits perfectly as it is a Last-In-First-Out (LIFO) data structure.
We evaluate the expression left-to-right and push operands onto the stack until we
encounter an operator, which we pop the top two values from the stack. We then evaluate
the operator, with the values as arguments and push the result back onto the stack.
For example, the infix expression “8 – ((1 + 2) * 2)” in RPN is:
8 1 2 + 2 * –

'''



def evalRPN(tokens):
    OPERATORS = set('+-*/')
    stack =[]
    for token in tokens:
        if token in OPERATORS:
            y = stack.pop()
            x = stack.pop()
            stack.append(eval(int(x),int(y),token))
        else:
            stack.append(token)
    return stack.pop()

def eval(x,y,operator):
    if operator =="+":
        return x + y
    elif operator =="-":
        return x -y
    elif operator == '*':
        return x*y
    elif operator == '/':
        return x//y

print(evalRPN("34*"))