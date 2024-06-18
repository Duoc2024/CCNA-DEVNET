# Función para solicitar datos y mostrarlos
def solicitar_datos():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    return nombre, apellido, edad

# Función para imprimir los datos ingresados
def imprimir_datos(nombre, apellido, edad):
    print("\nDatos ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")

# Llamada a las funciones
if __name__ == "__main__":
    nombre, apellido, edad = solicitar_datos()
    imprimir_datos(nombre, apellido, edad)
