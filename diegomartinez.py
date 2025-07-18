datos={}


productos= {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],           
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10],
          '2175HD': [327990,4],
            'JjfFHD': [424990,1],
            'fgdxFHD': [664990,21],
            '123FHD': [290890,32],
            '342FHD': [444990,7],
            'GF75HD': [749990,2],
            'UWU131HD': [349990,1],
            'FS1230HD': [249990,0], 
}


def marcas_stock():
    cantidad=input("ingrese marca a consultar: ")
    
    if cantidad in productos:
        dato=datos[cantidad]
        if cantidad=="hp":
            print(f"el stock es :{dato['hp']}")
        if cantidad=="asus":
            print(f"el stock es :{dato['Asus']}")

    elif not datos:
        print("el stock es 0")



def busqueda_por_precio():
    try:
        minimo=int(input("ingrese precio minimo: "))
        maximo=int(input("ingrese precio maximo: "))
        resultado=[]
        for modelo,(precio,inventario)in stock.items():
            if inventario>0 and minimo <= maximo:
                marca= productos[modelo][0]
                resultado.append(f"{marca}--{modelo}")
            if resultado:
                for item in sorted(resultado):
                    print(item)
            else:
                print("no hay en ese rango")
            break
    except ValueError:
        print("debe ingresar valores enteros!!")


def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0]=nuevo_precio
        return True
    

while True:

    print("*****Menu Principal*****")
    print("1.Stock Marca")
    print("2.Busqueda por precio")
    print("3.Actualizar precio")
    print("4.Salir")


    opcion=input("Ingrese Opcion: ")

    if opcion=="1":
        marcas_stock()                     
    elif opcion=="2":
        busqueda_por_precio()

        print()
    elif opcion=="3":
        while True:
            modelo=input("ingrese modelo a actualizar: ")
            try:
                nuevo_precio=int(input("ingrese el nuevo precio "))
                if actualizar_precio(modelo,nuevo_precio):
                    print("presio actualizado")
                    reintentar=input("quiere reintentar (si/no): ")
                    if reintentar !="si":
                        break
                    else: 
                        print("ingrese un skua valido")
            except ValueError:
                print("ingrese un valor valido")



    elif opcion=="4":
        print("Programa finalizado")
        break
