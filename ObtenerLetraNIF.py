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
dni = "1"
while True:
    dni = input("\nIntroduzca el número de DNI del que desea saber su letra: (0 para salir) » ")
    if dni == "0":
        print("\nHasta pronto! 👋")
        print("Por cortesia de: Jose Miguel Redondo | ironet.jmr@gmail.com")
        print("\n")
        break
    elif dni != "0":
        print("\nLa letra para el número de DNI introducido es la " + miTupla[int(dni)%23])
        print("✅ Obteniendo el NIF: "+dni+miTupla[int(dni)%23])
    else:
        print("Por cortesia de: Jose Miguel Redondo | ironet.jmr@gmail.com")
        print("\n")
