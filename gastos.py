from datetime import datetime
import csv
import os

tipo_categoria={
    1:"Comida",
    2:"Transporte",
    3:"Escuela",
    4:"Casa",
    5:"Otros"
    
}

while True:
    print("\n¿Qué quieres hacer?")
    print("1 - Agregar gasto")
    print("2 - Ver resumen")
    print("3 - Ver lista completa")
    print("4 - Salir")
    
    
    opcion=input("\nElige una opcion: ")
    
    if opcion == "1":
        now=datetime.now()
        day = now.day                   
        month = now.month
        year= now.year

        fecha=f"{day}-{month}-{year}"


        while True:
            try:
                
                print("Elige una categoría")
                print("1 - Comida")
                print("2 - Transporte")
                print("3 - Escuela")
                print("4 - Casa")
                print("5 - Otro")
                opcion_2=int(input("\nCategoría: "))
               
                categoria=tipo_categoria[opcion_2]
                
                descripcion=input("\nIngresa una descripción: ")
                monto=int(input("\nIngresa el monto gastado: "))
            except (ValueError,KeyError):
                print("Elige una categoría válida o ingresa un número en el monto")
            else:
                break   





        archivo_existe = os.path.exists("datos.csv")

        with open("datos.csv","a",newline="",encoding="utf-8")as file:
            writer= csv.writer(file)
            
            if not archivo_existe:
                writer.writerow(["Fecha","Categoría","Descripción","Monto"])
            
            writer.writerow([fecha,categoria,descripcion,monto])
            
    elif opcion == "2":
        print("Resumen de gastos:\n")
        with open("datos.csv","r",encoding="utf-8") as archivo:
        
            datos=csv.reader(archivo)
            
            
            
            next(datos)
            
            totales= {}
            for lista in datos:
                monto=int(lista[3])
                if lista[1] in totales:
                    totales[lista[1]]+=monto
                    
                else:
                        totales[lista[1]]=monto
            monto_total=0
            for categoria,monto in totales.items():
                print(f"{categoria.ljust(15)}${monto}")
                monto_total+=monto
            print("-----------------------")
            
            print(f"{"Total".ljust(15)}${monto_total}")
    elif opcion == "3":
        print("Lista completa:\n")
        with open("datos.csv","r",encoding="utf-8") as archivo:
        
            datos=csv.reader(archivo)
            for fila in datos:
                print(fila)
        
    elif opcion == "4":
        break
    else:
        print("Opcion invalida, intente de nuevo")