#https://www.python.org/

#diferentes sintaxis de crear comentarios.

#esto es un comentario, en una línea.
" esto es un comentario en una línea, con comillas dobles."
from operator import truediv

'esto es un comentario en una línea, con comillas sencillas.'
"""
esto es un comentario 
de varias lineas
con comillas dobles.
"""
'''
esto es un comentario 
de varias lineas
con comillas sencillas.
'''

#Crea una variable (y una constante si el lenguaje lo soporta).

mi_variable = "Mi variable"
# Multiples variables en una linea.
var_1, var_2, var_3 = "Variable 1" , "Variable 2" , "Variable 3"

# No existen constante en el lenguaje; sin embargo, por convenio se puede escribir en mayuscula
#y asi dar a entender que el valor de la variable no deberia ser modificado.

MI_CONSTANTE= "Mi contaste"

#Crea variables representando todos los tipos de datos primitivos
# del lenguaje (cadenas de texto, enteros, booleanos...).

texto = "Mi nombre" #str
enteros = 2025 #int
decimal = 1993.5 #float
boleano_0 = True #booleano
boleano_1 = False #booleano
ninguno = None # ninguno
complejo = 1 + 2j # complejo

#Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print("¡Hola, Python!")



