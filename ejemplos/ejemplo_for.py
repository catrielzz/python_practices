mi_lista = []
input_usuario = ""

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("Que necesitas comprar? (Escribe FIN para salir): ")

for item in mi_lista:
    print("Tengo que comprar: {}".format(item))

print("Esta es la lista de la compra, la cantidad de elementos que hay en la lista es {}".format(len(mi_lista)))