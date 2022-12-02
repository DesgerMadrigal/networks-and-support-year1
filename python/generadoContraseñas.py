from secrets import choice
from string import ascii_letters, ascii_uppercase, digits

caracteres = ascii_letters + ascii_uppercase + digits
longitud = 5  # La longitud que queremos
contraseña_aleatoria = ''.join(choice(caracteres) for caracter in range(longitud))
print("La cadena es: ", contraseña_aleatoria)