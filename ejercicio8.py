precio=input("Introduce un precio de un producto: ")

print("Euros: ",precio[:precio.find(".")], "Centimos: ",precio[precio.find("."):])