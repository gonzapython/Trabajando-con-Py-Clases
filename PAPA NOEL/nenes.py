from dummy_data import juguetes

class Nene(object):
    def __init__(self, nombre, edad, juguetes):
        self.nombre = nombre
        self.edad = edad
        self.juguetes = juguetes
        self.esta_registrado = False
        self.karma = 0
        self.lista_de_deseos = []

    def _listar_juguetes(self):
        print(" --------- LISTA de JUGUETES ----------- ")
        print("                                         ")
        for indice, juguete in enumerate(self.juguetes):
            if juguete['mostrar'] and self.karma >= juguete['karma']:
                print(f'{indice} .- {juguete}')
        print("                                         ")
        print(" --------------------------------------- ")


    def mostrar_lista(self):
        if self.esta_registrado:
            self._listar_juguetes()
        else:
            print('EL NIÑO NO ESTA REGISTRADO EN EL SISTEMA')

    def elegir_juguetes(self):
        elecion_juguete = int(input("Elige un juguete de la lista. Escribe el número y 'S' para acabar: > "))
        if elecion_juguete !='S':
            juguete_elegido = juguetes[elecion_juguete])
            self.lista_de_deseos.append(juguete_elegido)
            #self.lista_de_deseos.append(juguetes[elecion_juguete])

        print(" --------- JUGUETES ELEGIDOS ----------- ")
        print("                                         ")
        for indice, juguete in enumerate(self.lista_de_deseos):
            print(f'{indice} .- {juguete}')
        print("                                         ")
        print(" --------------------------------------- ")







