fecha = input("Escribe tu fecha de nacimiento: ")

dia = fecha[:fecha.find("/")]
ma = fecha[fecha.find("/")+1:]

mes = ma[:ma.find("/")]
año = ma[ma.find("/")+1:]

print(dia)
print(mes)
print(año)
