# Lexer
Analizador léxico para lenguaje Mini Pascal realizado en Python con la librería SLY.

Para ejecutar es necesario seguir el siguiente formato
python3 pascal.py [opcion] archivo [archivo]* <---- Para la ejecución en terminal unix

python pascal.py [opcion] archivo [archivo]* <---- Para ejecución en algún entorno de Python 3.6

Opciones:
Este es el analizador léxico; la primera fase del proyecto. Por esa razón, actualmente solo está habilitada la opción relacionada con el Lexer. Se ejecuta de cualquiera de las siguientes maneras:

python3 pascal.py -l archivo [archivo]*

python3 pascal.py --lex archivo [archivo]*

Con la ejecución de ese comando y teniendo los correspondientes archivos de código en Pascal, el programa pascal.py mostrará todos los tokens de los códigos ingresados como parámetro a la ejecución.
