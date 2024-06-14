"""
Conversor de temperatura:
de grados C 'celsius' a grados F 'Fahrenheit' y viceversa
____________________________________________________________
El 1.8 es la diferencia del punto de congelacion a 32 grados
y el punto de ebullicion a 212 grados Fahrenheit;
212-32=180, entonces; 180/100=1.8
"""
# AUTOR: Jose Miguel Redondo Romero

while True:
    try:
        print("\n╔═══════════════════════════════════════╗")
        print("║     ¿Que medida desea convertir?      ║")
        print("╚═══════════════════════════════════════╝")
        grados = input("\nIntroduzca 'C' para Celsius o 'F' para Fahrenheit » | utilice 'S' para Salir » ")

        if grados == "S":
            print("\nHasta pronto! 👋")
            print("Por cortesia de: Jose Miguel Redondo | ironet.jmr@gmail.com")
            print("\n")
            break
        elif grados == "C":
            valor = float(input("Introduzca el valor de los ºC que desea convertir a ºF: » "))
            resultado = float(valor) * 1.8 + 32
            print("✅ El valor "+ str(valor)+" ºC Celsius = "+str(resultado)+" ºF Fahrenheit")
        elif grados == "F":
            valor = float(input("Introduzca el valor de los ºF que desea convertir a ºC: » "))
            resultado = (float(valor) - 32) / 1.8
            print("✅ El valor "+ str(valor)+" ºF Fahrenheit = "+str(resultado)+" ºC Celsius")
        else:
            print("❌ Por favor utilice una entrada correcta")
            print("C para convertir ºC a ºF")
            print("F para convertir ºF a ºC")
            print("S para Salir/Abandonar el programa")
            print("\n")
    except ValueError:
        print("❌ Por favor, introduzca un valor númerico")
