#AUTOR: Jose Miguel Redondo Romero
#EMAIL: ironet.jmr@gmail.com

#Con esta clase definimos la tarea y damos por defecto, el estado de "pendiente" cuando la creamos. 
class Tarea:
    def __init__(self, nbtarea):            
        self.nbtarea = nbtarea      
        self.iscompletada = False             

#Esta clase es se utilizará para incorporar los/as métodos/opciones de menú de las tareas 
class Menu_tarea:                         
    def __init__(self):                     
        self.tareas = []                    

    # Método para añadir una nueva tarea
    def añadir_tarea(self, nbtarea):
        tarea = Tarea(nbtarea)          
        self.tareas.append(tarea)           
        print("\033[32m✅ Has agregado la tarea correctamente: \033[0m", tarea.nbtarea)

    # Método para eliminar una tarea con la excepción si la posición introducida no existe
    def eliminar_tarea(self, numero_tarea):
        try:
            tarea_eliminada = self.tareas.pop(numero_tarea - 1)
            print(f"\033[32m✅ Tarea '{tarea_eliminada.nbtarea}' eliminada.\033[0m")
        except IndexError:
            print("\033[31m❌ Por favor, introduce una posición correcta.\033[0m")

    # Método para completar una tarea con la excepción si la entrada es incorrecta.       
    def completar_tarea(self, numero_tarea):
        try:                                                       
            tarea = self.tareas[numero_tarea - 1]                   
            if tarea.iscompletada:
                print("\033[31m❌ Esta tarea ya está como completada.\33[0m")
            else:
                tarea.iscompletada = True
                print("\033[32m✅ Tarea marcada como completada: \033[0m", tarea.nbtarea)
        except IndexError:
            print("\033[31m❌ Por favor, introduce una posición correcta.\033[0m")
    
    # Método para cambiar una tarea completada a pendiente con la excepción si error
    def marcarpte_tarea(self, numero_tarea):
        try:
            tarea = self.tareas[numero_tarea - 1]
            if not tarea.iscompletada:
                print("\033[31m❌ Esta tarea ya está como pendiente.\033[0m")
            else:
                tarea.iscompletada = False
                print("\033[32m✅ Tarea cambiada a pendiente: \033[0m", tarea.nbtarea)
        except IndexError:
            print("\033[31m❌ Por favor, introduce una posición correcta.\033[0m")

    # Método que nos muestra la lista de tareas
    def muestralista_tareas(self):
        if not self.tareas:
            print("\033[31m❌ Aún no dispones de tareas, añade las tareas que necesites previamente usando la opción 1.\33[0m")
        else:
            print("   Listado de tareas y estado")
            print("   ══════════════════════════")
            for i, tarea in enumerate(self.tareas, 1):
                if tarea.iscompletada:
                    estado = "\033[32mCompletada\033[0m"
                else:
                    estado = "\033[31mPendiente\033[0m"
                print(f"{i}. {tarea.nbtarea} 👉 {estado}")

""" 
Con if __name__ == "__main__":  verificamos si el script se está
ejecutando como un programa independiente.
Si es así se ejecutará creando una instancia de la clase Menu_tarea
permitiendo al usuario interactuar con el sistema.
"""
if __name__ == "__main__":
    gestor = Menu_tarea()
    
    # Función principal de interacción con el usuario
    while True:                                         
        print("\n╔═══════════════════════════════════════╗")
        print("║       \033[34mTASKS ADMINISTRATION MENU\033[0m       ║")
        print("╚═══════════════════════════════════════╝")
        print("➀ Añadir una tarea")
        print("➁ Eliminar una tarea")
        print("   ➂ Marcar estado tarea como COMPLETADA")
        print("   ➃ Marcar estado tarea como PENDIENTE")
        print("      ➄ Mostrar tareas y estado")
        print("      ➅ Exit/Salir")
        
        opcion = input("\033[34mSelecciona una opción (valores 1 a 6): \033[0m")
        #Creación de una nueva tarea
        if opcion == "1":
            nbtarea = input("\033[34mIntroduce una nueva tarea: \033[0m")
            gestor.añadir_tarea(nbtarea)
        #Borrado de una tarea, muestra la lista y estados y solicita cual es la que se debe eliminar
        elif opcion == "2":
            if gestor.tareas:
                gestor.muestralista_tareas()
                numero_tarea = int(input("\033[34m¿Qué tarea quieres eliminar?: \033[0m"))
                gestor.eliminar_tarea(numero_tarea)
            else:
                print("\033[32m🏁 Enhorabuena, no tienes tareas pendientes.\033[0m")
        #Para marcar como completada la tarea, muestra la lista de tareas con su estado y solicita el id de la que hay que completar
        elif opcion == "3":
            if gestor.tareas:
                gestor.muestralista_tareas()
                numero_tarea = int(input("\033[34m¿Qué tarea quieres marcar como completada?: \033[0m"))
                gestor.completar_tarea(numero_tarea)
            else:
                print("\033[32m🏁 Enhorabuena, no tienes tareas pendientes.\033[0m")
        #Pasar una tarea de Completada a Pendiente
        elif opcion == "4":
            if gestor.tareas:
                gestor.muestralista_tareas()
                numero_tarea = int(input("\033[34m¿Qué tarea quieres marcar como pendiente?: \033[0m"))
                gestor.marcarpte_tarea(numero_tarea)
            else:
                print("\033[32m🏁 Enhorabuena, no tienes tareas pendientes.\033[0m")
        #Muestra las tareas
        elif opcion == "5":
            gestor.muestralista_tareas()
        #Salida del programa
        elif opcion == "6":
            print("\033[36mHasta pronto! 👋\33[0m")
            break
        else:
            print("\033[31m❌ Por favor introduzca una opción válida (valores permitidos de '1' a '6') \033[0m")