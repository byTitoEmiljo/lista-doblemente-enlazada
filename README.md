# **lista-doblemente-enlazada**

Este proyecto es una implementación de una lista doblemente enlazada en Python, diseñada para almacenar información sobre libros. Cada nodo de la lista contiene el nombre del libro, el autor y el precio. Se puede navegar por la lista hacia adelante y hacia atrás, mostrando la información de cada libro.

### Características
* Añadir libros a la lista con su nombre, autor y precio.
* Navegar por la lista hacia adelante y hacia atrás.
* Mostrar la información del libro actual en la lista.

### Instalación y Ejecución

1. Clona el repositorio: \
   `git clone https://github.com/tu_usuario/lista-doble-enlazada-libros.git`
3. Navega al directorio del proyecto: \
   `cd lista-doble-enlazada-libros`
5. Ejecuta el script: \
   `python main.py`

### Uso
1. Al iniciar el programa, se te pedirá que ingreses la cantidad de libros que deseas agregar.
2. Ingresa el nombre, autor y precio de cada libro.
3. Después de agregar los libros, podrás navegar por la lista utilizando las teclas:
   * `a` para moverte al libro anterior.
   * `b` para moverte al siguiente libro.
   * `q` para salir del programa.
  
### Ejemplo de Uso
```
Cuantos libros agregará: 3

3 Libros
Libro #1

Nombre del Libro: El Quijote
Nombre del Autor: Miguel de Cervantes
Precio del libro: 25

3 Libros
Libro #2

Nombre del Libro: Cien Años de Soledad
Nombre del Autor: Gabriel García Márquez
Precio del libro: 30

3 Libros
Libro #3

Nombre del Libro: La Sombra del Viento
Nombre del Autor: Carlos Ruiz Zafón
Precio del libro: 20
```
Navegación por la lista:
```
Nombre: El Quijote
Autor: Miguel de Cervantes
Precio: 25

←"a"        "d"→
        "q"(salir)
```
