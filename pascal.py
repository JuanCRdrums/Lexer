from paslex import *
import sys
import os

if __name__ == '__main__':
    file = "tests/charconst.pas"
    lexer = PascalLexer()
    if len(sys.argv) > 1:
        files = sys.argv[2:len(sys.argv)]
        if sys.argv[1] == "-l" or sys.argv[1] == "--lex":
            for f in files:
                if os.path.isfile(f):
                    printLex(f,lexer)
                else:
                    print("ERROR: The file %r does not exist" % f)
                print("-------------------------------------\n")
