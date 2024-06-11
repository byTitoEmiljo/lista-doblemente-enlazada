import os


class Nodo:
    def __init__(self, nombre, autor, precio):
        self.libro = [nombre, autor, precio]
        self.sig = None
        self.ant = None


class lisDobEnlaze:
    def __init__(self):
        self.ini = None
        self.act = None

    def add(self, nombre, autor, precio):
        newNodo = Nodo(nombre, autor, precio)

        if self.ini is None:
            self.ini = newNodo
            self.act = newNodo
            return

        fin = self.ini

        while fin.sig:
            fin = fin.sig
        fin.sig = newNodo
        newNodo.ant = fin

    def printList(self, direccion=None):
        if direccion == 'a':
            if self.act and self.act.ant:
                self.act = self.act.ant
        elif direccion == 'd':
            if self.act and self.act.sig:
                self.act = self.act.sig

        print(f"Nombre: {self.act.libro[0]}\n"
              f"Autor: {self.act.libro[1]}\n"
              f"Precio: {self.act.libro[2]}")


def main():
    listaDob = lisDobEnlaze()
    os.system('cls')
    cantLib = int(input('Cuantos libros agregará: '))

    for i in range(cantLib):
        print(f'{cantLib} Libros\nLibro #{i + 1}\n')
        lib = input('Nombre del Libro: ')
        aut = input('Nombre del Autor: ')
        pre = int(input('Precio del libro: '))
        listaDob.add(lib, aut, pre)
        os.system('cls')

    while True:
        os.system('cls')
        listaDob.printList()
        direc = input('←"a"\t\t"d"→\n\t"q"(salir)\n')
        if direc.lower() == 'q':
            break
        elif direc.lower() == 'a' or direc.lower() == 'd':
            listaDob.printList(direc)


if __name__ == '__main__':
    main()
