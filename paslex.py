from sly import Lexer

class PascalLexer(Lexer):

    tokens = { ID, INTCONST, CHARCONST, SPECIAL, PREID }

    ignore_comment = r'\(\*.*\*\)|{.*}|//.*'
    ignore_newline = r'\n+'

    ID = r'[a-zA-z][a-zA-Z0-9]*'
    INTCONST = r'[0-9]+'
    CHARCONST = r'\'.*\'|".*"'
    SPECIAL = r''
