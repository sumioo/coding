#coding:utf-8
'''
a calculator base on converting infix to RPN

'''
from __future__ import division
import re
from operator import add,sub,mul,div,mod,pow

#Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

#Supported operators
OPERATORS = {
    '+' : (0, LEFT_ASSOC,add),
    '-' : (0, LEFT_ASSOC,sub),
    '*' : (5, LEFT_ASSOC,mul),
    '/' : (5, LEFT_ASSOC,div),
    '%' : (5, LEFT_ASSOC,mod),
    '^' : (10, RIGHT_ASSOC,pow)
}

MATHMATIC_SYMBOL='+*/%)(^-'

#split digit and symbol
def split_expr(expression):
    out=re.findall('[\d.]+|[%s]' % MATHMATIC_SYMBOL,expression)
    for idx,val in enumerate(out):
        #process negative
        if val == '(' and out[idx+1] == '-':
            out[idx+1]='-'+out[idx+2]
            del out[idx+2]
    return out

#check the input expression's validation
def simple_check(expression):                                      #check the input expression's validation
    invalid_symbol=re.findall('[^\d.%s]' % MATHMATIC_SYMBOL,expression)
    bracket_is_equal=expression.count('(') == expression.count(')')
    operator_is_equal_digit=len(re.findall('[^(]([-+*/^%])',expression)) == len(re.findall('[\d.]+',expression))-1
    division_is_not_zero=re.findall('/0',expression)
    return not invalid_symbol and bracket_is_equal and operator_is_equal_digit and not division_is_not_zero

#Test if a certain token is operator
def is_operator(token):
    return token in OPERATORS.keys()

#Test the associativity type of a certain token
def is_associative(token, assoc):
    if not is_operator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc

#Compare the precedence of two tokens
def cmp_precedence(token1, token2):
    if not is_operator(token1) or not is_operator(token2):
        raise ValueError('Invalid tokens: %s %s' % (token1, token2))
    return OPERATORS[token1][0] - OPERATORS[token2][0]

#Transforms an infix expression to RPN
def infix_to_RPN(tokens):
    out = []
    stack = []
    #For all the input tokens read the next token
    for token in tokens:
        if is_operator(token):
            # If token is an operator
            while len(stack) != 0 and is_operator(stack[-1]):
                if (is_associative(token, LEFT_ASSOC) and cmp_precedence(token, stack[-1]) <= 0) or (is_associative(token, RIGHT_ASSOC) and cmp_precedence(token, stack[-1]) < 0):
                    out.append(stack.pop())
                    continue
                break
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        else:
            out.append(token)
    while len(stack) != 0:
        out.append(stack.pop())
    return out

#calculrate RPN expression
def calculate_RPN(list_RPN):
    out=[]
    operators=OPERATORS.keys()
    try:
        for token in list_RPN:
            if token not in operators:
                out.append(token)
            else:
                token1=out.pop()
                token2=out.pop()
                result=OPERATORS[token][2](float(token2),float(token1))
                out.append(result)
    except IndexError:
        return 'Invalid expr'
    return out[0]


def main(expression):
    if not simple_check(expression):
        return 'Invalid expression'
    tokens=split_expr(expression)
    RPN_list=infix_to_RPN(tokens)
    #print RPN_list
    return calculate_RPN(RPN_list)


if __name__ == '__main__':
        expression=['(1+2.0-1)+(-7+7)*5','2-5+(-1)^2']
        for i in expression:
            #print eval(i)
            print main(i)
            #s=split_expr(i)
            #print s
            #print infix_to_RPN(s)
