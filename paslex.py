from sly import Lexer

class PascalLexer(Lexer):

    keywords = { 'program', 'var', 'array', 'of', 'procedure', 'begin', 'end',
                'write', 'read', 'if', 'then', 'else', 'while', 'do', 'not',
                'or', 'div', 'and'}
    tokens = { ID, INTCONST, CHARCONST, *{kw.upper() for kw in keywords},
                PLUS, MINUS, TIMES, EQ, NE, LT, GT, LE, GE, LPAR, RPAR, LBR,
                RBR, ASSIGN, DOT, COMA, SEMICOLON, COLON, RANGE }

    ignore = r' \t'

    ignore_comment = r'\(\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*?\*+\)'
    ignore_newline = r'\n+'

    INTCONST = r'[0-9]+'
    CHARCONST = r'\'.*\'|".*"'
    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    EQ = r'='
    NE = r'<>'
    LT = r'<'
    GT = r'>'
    LE = r'<='
    GE = r'>='
    LPAR = r'\('
    RPAR = r'\)'
    LBR = r'\['
    RBR = r'\]'
    ASSIGN = r':='
    DOT = r'\.'
    COMA = r','
    SEMICOLON = r';'
    COLON = r':'
    RANGE : r'\.\.'

    @_(r'[a-zA-z][a-zA-Z0-9]*')
    def ID(self,t):
        if t.value.lower in self.keywords:
            t.type = t.value.upper()
        return t

if __name__ == '__main__':
    file = open("tests/bubbleSort.pas", "r")
    code = file.read()
    lexer = PascalLexer()
    for tok in lexer.tokenize(code):
        print('type=%r, value=%r' % (tok.type, tok.value))
