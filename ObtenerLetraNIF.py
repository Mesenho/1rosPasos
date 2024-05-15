"""
Cálculo del dígito de control del NIF/NIE
El artículo 11 del Real Decreto 1553/2005, de 23 de  diciembre, establece que
el Documento Nacional de Identidad recogerá el número personal del DNI y carácter
de verificación correspondiente al número de Identificación Fiscal.

Para verificar el NIF de españoles residentes mayores de edad,
el algoritmo de cálculo del dígito de control es el siguiente:
Se divide el número entre 23 y el resto se sustituye por una
letra que se determina por inspección mediante la Tupla usada en este código:
"""
# AUTOR: Jose Miguel Redondo Romero
# creo una tupla con el valor de la letra en el orden correcto de acuerdo con la fórmula
miTupla = ("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")
dni = input("\nIntroduzca el número de DNI del que desea saber su letra: ")
print("\nLa letra para el número de DNI introducido es la " + miTupla[int(dni)%23])
print("\n✅ Obteniendo el NIF: "+dni+miTupla[int(dni)%23])
print("\nPor cortesia de: Jose Miguel Redondo | ironet.jmr@gmail.com")
print("\n")