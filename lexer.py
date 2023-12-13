from ply import *

tokens = (
    'ID',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
)

# Regras de expressões regulares para os tokens
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_ID(t):
    r'[a-z_0-9_]'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
