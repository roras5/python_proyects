def run(): 
    # A los diccionarios se accede por llaves, en vez de indices o index 
    my_dictionary = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # Al acceder a un elemento del diccionario se hace por llavesd y entre corchetes
    #print(my_dictionary['llave1'])
    poblacion_paises ={
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 4648111,
    }

    # Mostrar las llaves del diccionario, FUNCIONA SIN EL .keys
    #for paises in poblacion_paises.keys():
     #   print(paises)
    #Mostrar los valores asignados a dichas llaves, ES NECESARIO el .values
    #for habitantes in poblacion_paises.values():
        #print(habitantes)
    
    for paises, poblacion in poblacion_paises.items():
        print(paises + ' '+ str(poblacion))



if __name__ == '__main__':
    run()