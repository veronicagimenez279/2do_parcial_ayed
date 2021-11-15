from cola import Cola
from lista import Lista

class Arbol (object):

    def __init__(self, info = None, datos = None):
        self.info = info
        self.datos = datos 
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        """Devuelve True si el arbol vacio."""
        return self.info is None

    def altura (self, arbol):
        """Devuelve la altura de un nodo."""
        if (arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura (self):
        """Actualiza la altura de un nodo."""
        if (self is not None):
            alt_izq = self.altura(self.izq)
            alt_der = self.altura(self.der)
            self._altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

    def rotacion_simple (self, control):
        if (control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else: 
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura() 
        aux.actualizar_altura() 
        return aux

    def rotacion_doble (self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos = None): 
        """Inserta un dato clave al árbol y opcionalmente hay un campo datos en el que se puede insertar mas información."""
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden (self):
        """Realiza el barrido inorden del arbol.
        Los elementos se listan en orden ascendente (menor a mayor)."""
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.inorden()
            print (self.info, self.datos)
            if (self.der is not None):
                self.der.inorden()

    def postorden (self):
        """Realiza el barrido postorden del arbol.
        Los elementos se listan en orden descendente (mayor a menor)."""
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden (self):
        """Realiza el barrido preorden del arbol.
        Los elementos se listan en el orden en que fueron cargados."""
        if (self.info is not None):
            print (self.info, self._altura)
            if (self.izq is not None):
                self.izq.preorden()
            if (self.der is not None):
                self.der.preorden()         

    def busqueda (self, clave):
        """Devuelve la direccion del elemento buscado."""
        pos = None
        if (self.info is not None):
            if(self.info == clave):
                pos = self
            elif (clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif (self.der is not None):
                pos = self.der.busqueda(clave)
        return pos

    def busqueda_proximidad(self, clave):
        """Realiza una busqueda donde muestra todos los elementos que comiencen con 'clave'."""
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)

    def busqueda_por_coincidencia(self, clave):
        """Realiza una busqueda donde muestra todos los elementos que contienen 'clave' en su nombre."""
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_por_coincidencia(clave)
            if(clave in self.info):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_por_coincidencia(clave)

    def reemplazar (self):
        """Determina el nodo que remplazará al que se elimina."""
        aux = None
        if (self.der is None): 
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.reemplazar()
        return info, datos

    def eliminar_nodo (self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.reemplazar()
                    self.info = info_aux
                    self.datos = datos_aux
        self = self.balancear()
        self.actualizar_altura()
        return info, datos

    def barrido_por_nivel (self):
        """Realiza el barrido por nivel del arbol."""
        pendientes = Cola()
        pendientes.arribo(self)
        while (not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print (nodo.info)
            if (nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if (nodo.der is not None):
                pendientes.arribo(nodo.der)

    def barrido_por_nivel_huff (self):
        """Realiza el barrido por nivel del arbol con codigos de Huffman."""
        pendientes = Cola()
        pendientes.arribo(self)
        while (not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print (nodo.info, nodo.datos)
            if (nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if (nodo.der is not None):
                pendientes.arribo(nodo.der)               


    def mostrar_dinosaurio (self, codigo):
        """Muestra toda la informacion del dinosaurio con el codigo dado."""
        pos = self.busqueda(codigo)
        if (pos):
            print (' - Nombre:', pos.datos['nombre'])
            print (' - Codigo:', pos.datos['codigo'])
            print (' - Zona:', pos.datos['zona'])

    def mostrar_por_nombre (self, nombre):
        """Muestra a todos los dinosaurios de un nombre dado."""
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.mostrar_por_nombre(nombre)
            if (self.datos['nombre'] == nombre):
                print (self.info, '- Codigo:', self.datos['codigo'], '- Zona:', self.datos['zona'])
            if (self.der is not None):
                self.der.mostrar_por_nombre(nombre)


    def cambiar_nombre (self, nombre_viejo, nombre_nuevo):
        """Cambia el nombre original por el nombre_nuevo dado."""
        pos = self.busqueda(nombre_viejo)
        if (pos):
            nombre, datos = self.eliminar_nodo(nombre_viejo)
            datos['nombre'] = nombre_nuevo
            self = self.insertar_nodo(nombre_nuevo, datos)


    def mostrar_ubicacion_dinosaurio (self, dinosaurio):
        """Muestra la ubicacion de todos los dinosaurios con el nombre dado."""  
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.mostrar_ubicacion_dinosaurio(dinosaurio)
            if (self.datos['nombre'] == dinosaurio):
                print ('Zona', self.datos['zona'])
            if (self.der is not None):
                self.der.mostrar_ubicacion_dinosaurio(dinosaurio)

    def contador_dinosaurios (self, dinosaurio):
        """Cuenta cuantos dinosaurios hay del tipo dado."""
        cantidad = 0
        if (self.info is not None):
            if (self.info == dinosaurio):
                cantidad += 1
            if (self.izq is not None):
                cantidad += self.izq.contador_dinosaurios(dinosaurio)
            if (self.der is not None):
                cantidad += self.der.contador_dinosaurios(dinosaurio)
        return cantidad