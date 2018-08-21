from sly import Lexer

class PascalLexer(Lexer):

    keywords = { 'program', 'var', 'array', 'of', 'procedure', 'begin', 'end',
                'write', 'read', 'if', 'then', 'else', 'while', 'do', 'not',
                'or', 'div', 'and'}
    tokens = { ID, INTCONST, CHARCONST, *{kw.upper() for kw in self.keywords},
                PLUS, MINUS, TIMES, EQ, NE, LT, GT, LE, GE, LPAR, RPAR, LBR,
                RBR, ASSIGN, DOT, COMA, SEMICOLON, COLON, RANGE }

    ignore_comment = r'\(\*.*\*\)|{.*}|//.*'
    ignore_newline = r'\n+'

    INTCONST = r'[0-9]+'
    CHARCONST = r'\'.*\'|".*"'

    @_r'[a-zA-z][a-zA-Z0-9]*'
    def ID(self,t):
        if t.value.lower in self.keywords:
            t.type = t.value.upper()
        return t 
