from arbol_binario import Arbol
from grafo import Grafo
#! ------------------------- EJERCICIO ARBOL ------------------------- !#
# El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
# resolver los siguientes requerimientos:
# 1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
# conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
# por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
# distintos, los códigos no pueden ser repetidos (tenga cuidado);
# 2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
# código;
# 3. realizar un barrido en orden del árbol ordenado por nombre;
# 4. mostrar toda la información del dinosaurio 00792;
# 5. mostrar toda la información de todos los T-Rex que hay en la isla;
# 6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;
# 7. mostrar la ubicación de todos los Raptores que hay en la isla;
# 8. contar cuantos Diplodocus hay en el parque;
# 9. debe cargar al menos 15 elementos.

dinosaurios = Arbol()
dinosaurios_codigo = Arbol()

datos_dinosaurios = [{'nombre': 'T-Rex', 'codigo' : '00125', 'zona' : '6B'},
                     {'nombre': 'Raptor', 'codigo' : '00505', 'zona' : '3G'},
                     {'nombre': 'Sgimoloch', 'codigo' : '00745', 'zona' : '3H'},
                     {'nombre': 'Stegosaurus', 'codigo' : '00333', 'zona' : '3H'},
                     {'nombre': 'T-Rex', 'codigo' : '00191', 'zona' : '5A'},
                     {'nombre': 'T-Rex', 'codigo' : '00792', 'zona' : '8A'},
                     {'nombre': 'Raptor', 'codigo' : '00856', 'zona' : '1Z'},
                     {'nombre': 'Diplodocus', 'codigo' : '00111', 'zona' : '1Z'},
                     {'nombre': 'T-Rex', 'codigo' : '00112', 'zona' : '1B'},
                     {'nombre': 'Stegosaurus', 'codigo' : '00113', 'zona' : '1C'},
                     {'nombre': 'Raptor', 'codigo' : '00221', 'zona' : '2A'},
                     {'nombre': 'Stegosaurus', 'codigo' : '00333', 'zona' : '2V'},
                     {'nombre': 'Triceratops', 'codigo' : '00223', 'zona' : '3F'},
                     {'nombre': 'Diplodocus', 'codigo' : '00888', 'zona' : '4T'},
                     {'nombre': 'Raptor', 'codigo' : '00777', 'zona' : '5T'},
]

#! ---- PUNTO 2 ----!#
for dinosaurio in datos_dinosaurios:
    dinosaurios = dinosaurios.insertar_nodo(dinosaurio['nombre'], dinosaurio)

for dinosaurio in datos_dinosaurios:
    dinosaurios_codigo = dinosaurios_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

#! ---- PUNTO 3 ----!#
print('Barrido en orden del arbol ordenado por nombre:')
dinosaurios.inorden()
print()

#! ---- PUNTO 4 ----!#
print('Informacion del dinosaurio 00792')
dinosaurios_codigo.mostrar_dinosaurio('00792')
print()

#! ---- PUNTO 5 ----!#
print('Información de todos los T-Rex en la isla:')
dinosaurios.mostrar_por_nombre('T-Rex')
print()

#! ---- PUNTO 6 ----!#
dinosaurios.cambiar_nombre('Sgimoloch', 'Stygimoloch')
dinosaurios_codigo.cambiar_nombre('Sgimoloch', 'Stygimoloch')

# dinosaurios.inorden()
# dinosaurios_codigo.inorden()

#! ---- PUNTO 7 ----!#
print('Ubicacion de todos los raptores:')
dinosaurios.mostrar_ubicacion_dinosaurio('Raptor')
print()

#! ---- PUNTO 8 ----!#
# 8. contar cuantos Diplodocus hay en el parque;
cantidad = dinosaurios.contador_dinosaurios('Diplodocus')
print('La cantidad de Diplodocus en el parque es', cantidad)
print()

#! ------------------------- EJERCICIO GRAFO ------------------------- !#

# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# 4. encontrar el árbol de expansión mínima;
# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
# 6. debe utilizar un grafo no dirigido.

redes = Grafo(dirigido=False)

redes.insertar_vertice('Switch 1', data = 'Switch')
redes.insertar_vertice('Switch 2', data = 'Switch')
redes.insertar_vertice('Router 1', data = 'Router')
redes.insertar_vertice('Router 2', data = 'Router')
redes.insertar_vertice('Router 3', data = 'Router')
redes.insertar_vertice('Debian', data = 'Notebook')
redes.insertar_vertice('Red Hat', data = 'Notebook')
redes.insertar_vertice('Arch', data = 'Notebook')
redes.insertar_vertice('Ubuntu', data = 'PC')
redes.insertar_vertice('Mint', data = 'PC')
redes.insertar_vertice('Manjaro', data = 'PC')
redes.insertar_vertice('Parrot', data = 'PC')
redes.insertar_vertice('Fedora', data = 'PC')
redes.insertar_vertice('Guarani', data = 'Servidor')
redes.insertar_vertice('MongoDB', data = 'Servidor')
redes.insertar_vertice('Impresora', data = 'Impresora')

redes.insertar_arista(17, 'Switch 1', 'Debian')
redes.insertar_arista(18, 'Switch 1', 'Ubuntu')
redes.insertar_arista(22, 'Switch 1', 'Impresora')
redes.insertar_arista(80, 'Switch 1', 'Mint')
redes.insertar_arista(29, 'Switch 1', 'Router 1')
redes.insertar_arista(37, 'Router 1', 'Router 2')
redes.insertar_arista(43, 'Router 1', 'Router 3')
redes.insertar_arista(50, 'Router 2', 'Router 3')
redes.insertar_arista(25, 'Router 2', 'Red Hat')
redes.insertar_arista(9, 'Router 2', 'Guarani')
redes.insertar_arista(61, 'Switch 2', 'Router 3')
redes.insertar_arista(40, 'Switch 2', 'Manjaro')
redes.insertar_arista(12, 'Switch 2', 'Parrot')
redes.insertar_arista(5, 'Switch 2', 'MongoDB')
redes.insertar_arista(56, 'Switch 2', 'Arch')
redes.insertar_arista(3, 'Switch 2', 'Fedora')

# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
pos = redes.buscar_vertice('Red Hat')
print('Barrido en profundidad y amplitud paritendo de Red Hat:')
redes.barrido_profundidad(pos)
redes.marcar_no_visitado()
print()
redes.barrido_amplitud(pos)
redes.marcar_no_visitado()
print()
pos = redes.buscar_vertice('Debian')
print('Barrido en profundidad y amplitud paritendo de Debian:')
redes.barrido_profundidad(pos)
redes.marcar_no_visitado()
print()
redes.barrido_amplitud(pos)
redes.marcar_no_visitado()
print()
pos = redes.buscar_vertice('Arch')
print('Barrido en profundidad y amplitud paritendo de Arch:')
redes.barrido_profundidad(pos)
redes.marcar_no_visitado()
print()
redes.barrido_amplitud(pos)
redes.marcar_no_visitado()
print()

# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
redes.camino_mas_corto('Debian', 'MongoDB')
print()
redes.camino_mas_corto('Red Hat', 'MongoDB')
print()

# 4. encontrar el árbol de expansión mínima;
redes.arbol_expansion_minimo()
print()


# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
redes.eliminar_vertice('Impresora')
redes.barrido_profundidad(0)