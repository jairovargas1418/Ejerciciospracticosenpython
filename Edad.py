# Programa para verificar si un usuario es mayor de edad en Python



def obtener_edad():
    """Solicita la edad del usuario y la valida."""
    while True:
        try:
            edad = int(input("Por favor, ingresa tu edad: "))
            if edad < 0:
                print("La edad no puede ser un número negativo. Intenta nuevamente.")
            else:
                return edad
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def verificar_mayoria_edad(edad):

    """Determina si el usuario es mayor de edad y muestra un mensaje personalizado."""
    if edad >= 18:
                print(""" Eres mayor de edad. ¡Bienvenido al mundo adulto! 
        Disfruta de tu independencia y responsabilidades.""")
                # Verifica si el usuario tiene 60 años o más
                if edad >= 60:
                    print("¡Además, eres una persona con gran experiencia! Tu conocimiento es invaluable.")
    else:
        print("No eres mayor de edad. Aprovecha esta etapa para aprender, disfrutar y crecer.")
        if edad <= 12:
            print("¡ hola Maria Paula  Eres muy joven! Sigue descubriendo el mundo y aprendiendo cosas nuevas.")

# Programa principal
if __name__ == "__main__":
    edad_usuario = obtener_edad()  # Obtiene la edad validada del usuario
    verificar_mayoria_edad(edad_usuario)  # Verifica la edad y muestra el mensaje adecuado