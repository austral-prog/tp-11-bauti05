def read_file_to_dict(filename):

    ndict ={}

    try:

        with open(filename,"r") as archivo:

            lector = archivo.read()
            datos = lector.split(";")

            for i in datos:
                if i:
                    producto, valor = i.split(":")
                    valor = float(valor)

                    if producto in ndict:
                        ndict[producto].append(valor)
                    else:
                        ndict[producto] = [valor]

    except FileNotFoundError as error:
        raise FileNotFoundError("no se pudo encontrar el archivo")

    return ndict



def process_dict(data):
 
    for producto, ventas in data.items():
        total = sum(ventas)
        promedio = total / len(ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
