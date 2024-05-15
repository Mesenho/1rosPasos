"""
La clase empleado contiene los datos que serán compartidos con sus clases hijas.
La clase empleado contiene un constructor para iniciar sus atributos.
Los datos utilizados son: nombre completo, dni y teléfono.
Cada atributo de la clase cuenta con sus respectivos get y set.
"""

class Empleado:

    def __init(self, nombre, dni, telefono):
        self._nombre = nombre
        self._dni = dni
        self._telefono = telefono

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_dni(self, dni):
        self._dni = dni

    def get_dni(self):
        return self._dni
    
    def set_telefono(self, telefono):
        self._telefono

    def get_telefono(self):
        return self._telefono
    
"""
» Clase de empleado por tiempo DEFINIDO
Esta clase hereda de la clase empleado.
Sus nuevos atributos son: Númeo de plaza, Salario base, Duración de contrato en meses.

Además cuenta con un método que calcula el salario total. El empleado recibe un aumento del 2%
sobre su salario base.
"""

class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, dni, telefono, numplaza, salariobase, duracioncontrato):
        #constructor de la clase empleado
        super().__init__(nombre, dni, telefono)
        #nuevos atributos
        self._numplaza=numplaza
        self._salariobase=salariobase
        self._duracioncontrato=duracioncontrato

    def set_numplaza(self, numplaza):
        self._numplaza=numplaza

    def get_numplaza(self):
        return self._numplaza
    
    def set_salariobase(self, salariobase):
        self._salariobase=salariobase

    def get_salariobase(self):
        return self._salariobase
    
    def set_duracioncontrato(self, duracioncontrato):
        self._duracioncontrato=duracioncontrato

    def get_duracioncontrato(self):
        return self._duracioncontrato
    
    # calculo del salario total con subida 2%
    def calcularsalariototal(self):
        return self._salariobase + (self._salariobase * 0.02)

"""
» Clase de empleado por tiempo INDEFINIDO
Hereda de la clase Empleado y sus nuevos atributos son
- Número de plaza
- Salario base
- Categoría (1, 2, 3)
Además, cuenta con un método que calcula el salario total. Los empleados reciben un aumento en base
a su categoría como sigue:
-Categoria 1 = 3%
-Categoria 2 = 5%
-Categoria 3 = 8%
"""

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, dni, telefono, numplaza, salariobase, categoria):
        #constructor de la clase Empleado
        super().__init__(nombre, dni, telefono)
        #nuevos atributos
        self._numplaza=numplaza
        self._salariobase=salariobase
        self._categoria=categoria

    def set_numplaza(self, numplaza):
        self._numplaza=numplaza

    def get_numplaza(self):
        return self._numplaza
    
    def set_salariobase(self, salariobase):
        self._salariobase=salariobase

    def get_salariobase(self):
        return self._salariobase

    def set_categoria(self, categoria):
        self._categoria=categoria

    def get_categoria(self):
        return self._categoria
    
    #calculo del salario con subida en base a categoria del empleado
    def calcularsalariototal(self):
        if self._categoria==1:
            return self._salariobase + (self._salariobase * 0.03)
        elif self._categoria==2:
            return self._salariobase + (self._salariobase * 0.05)
        elif self._categoria==3:
            return self._salariobase + (self._salariobase * 0.08)
        else:
            return self._salariobase

"""
Empleado SUBCONTRATADO
Esta clase hereda de la clase empleado. El nuevo atributo es Empresa Responsable.
"""

class EmpleadoSubcontratado(Empleado):
    def __init__(self, nombre, dni, telefono, empresaresponsable):
        #constructor de la clase Empleado
        super().__init__(nombre, dni, telefono)
        #nuevo atributo para la clase de empleado subcontratado
        self._empresaresponsable = empresaresponsable
    
    def set_empresaresponsable(self, empresa):
        self._empresaresponsable = empresa
    
    def get_empresa(self):
        return self._empresaresponsable

"""
Ejecución del código

el siguiente código ejecuta las clases creadas anteriormente. 7 tipos de empleados desglosados
de la siguiente manera:
-2 subcontratados
-2 contratados
-3 indefinidos con diferentes categorias x el cálculo del nuevo salario base
"""

#empleados subcontratados
subcontratado1=EmpleadoSubcontratado("nombre1 ape1 ape2", 123456, 91000001, "Coca-Cola")
subcontratado2=EmpleadoSubcontratado("nombre2 ape2 ape2", 987654, 91000002, "Pepsi")

print("*** Empleados Subcontratados ***")
print("/n****Empleado 1****")
print("Nombre: "+ subcontratado1.get_nombre() +
"\n DNI: " + str(subcontratado1.get_dni()) +
"\nEmpresa Responsable: " + subcontratado1.get_empresaresponsable())
print("/n****Empleado 2****")
print("Nombre: "+ subcontratado2.get_nombre() +
"\n DNI: " + str(subcontratado2.get_dni()) +
"\nEmpresa Responsable: " + subcontratado2.get_empresaresponsable())

#empleados por tiempo definido
empleado1=EmpleadoDefinido("nombre3 ape3 ape3", 1000001, 913025478, 3, 25000, 6)
empleado2=EmpleadoDefinido("nombre4 ape4 ape4", 70123456, 679001122, 4, 18000, 3)

print("\n*** Empleados de tiempo Definido ***")
print("\n****Empleado1****")
print("Nombre: " +empleado1.get_nombre() + 
"\nDNI: " + str(empleado1.get_dni()) +
"\nNúmero de plaza: " + empleado1.get_numplaza() +
"\nDuración de contrato: " + empleado1.get_duracioncontrato() + " meses" +
"\nSalario con subida: " + str(empleado1.calcularsalariototal()))

print("\n****Empleado2****")
print("Nombre: " +empleado2.get_nombre() + 
"\nDNI: " + str(empleado2.get_dni()) +
"\nNúmero de plaza: " + empleado2.get_numplaza() +
"\nDuración de contrato: " + empleado2.get_duracioncontrato() + " meses" +
"\nSalario con subida: " + str(empleado2.calcularsalariototal()))

#empleados por tiempo indefinido
empleadoCat1=EmpleadoIndefinido("nombre5 ape5 ape5", 74012459, 649234587, 1, 36000, 1)
empleadoCat2=EmpleadoIndefinido("nombre6 ape6 ape6", 12568556, 911112233, 2, 38540, 1)
empleadoCat3=EmpleadoIndefinido("nombre7 ape7 ape7", 8000001, 741222689, 3, 41150, 1)

print("\n*** Empleados por tiempo INDEFINIDO ***")
print("\n****Empleado 1****")
print("Nombre: " + empleadoCat1.get_nombre() + 
"\nDNI: " + str(empleadoCat1.get_dni()) +
"\nTeléfono: " + str(empleadoCat1.get_telefono()) +
"\nNúmero de Plaza: " + str(empleadoCat1.get_numplaza) +
"\nCategoría: " + str(empleadoCat1.get_categoria) +
"\nSalario con subida: " + str(empleadoCat1.calcularsalariototal()))

print("\n****Empleado 2****")
print("Nombre: " + empleadoCat2.get_nombre() + 
"\nDNI: " + str(empleadoCat2.get_dni()) +
"\nTeléfono: " + str(empleadoCat1.get_telefono()) +
"\nNúmero de Plaza: " + str(empleadoCat2.get_numplaza) +
"\nCategoría: " + str(empleadoCat2.get_categoria) +
"\nSalario con subida: " + str(empleadoCat2.calcularsalariototal()))

print("\n****Empleado 3****")
print("Nombre: " + empleadoCat3.get_nombre() + 
"\nDNI: " + str(empleadoCat3.get_dni()) +
"\nTeléfono: " + str(empleadoCat3.get_telefono()) +
"\nNúmero de Plaza: " + str(empleadoCat3.get_numplaza) +
"\nCategoría: " + str(empleadoCat3.get_categoria) +
"\nSalario con subida: " + str(empleadoCat3.calcularsalariototal()))