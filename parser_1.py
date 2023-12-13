from ply import yacc
from lexer import lexer, tokens
from vasco2 import *

win = GraphWin("Circuito", 1, 1)

def p_expression(p):
    '''
    expression : term
               | expression OR term
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == 'OR':
        p[0] = DrawGate(win, p[1],'or', p[3])

def p_term(p):
    '''
    term : factor
         | term AND factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] =='AND':
        p[0] = DrawGate(win, p[1],'and', p[3])

def p_factor(p):
    '''
    factor : ID
           | NOT factor
           | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        p[0] = DrawVar(win, p[1])#VASCO
    elif p[1] =='NOT':
        p[0] = DrawNot(win, p[2])
    elif p[1] == '(':
        p[0] = p[2]

start = 'expression'

def p_error(p):
    print(f"Syntax error at '{p.value}'")

def bool_variable(variable):
    return bool(variable)

parser = yacc.yacc()

