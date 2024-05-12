from datetime import datetime

class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.libros_prestados = []

    def prestar_libro(self, libro, fecha_prestamo):
        self.libros_prestados.append((libro, fecha_prestamo))

    def devolver_libro(self, libro):
        for prestamo in self.libros_prestados:
            if prestamo[0] == libro:
                self.libros_prestados.remove(prestamo)
                return True
        return False
        
class Libro:
    def __init__(self, titulo, categoria):
        self.titulo = titulo
        self.categoria = categoria
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def borrar_usuario(self, usuario):
        if not any(prestamo[0].prestado for user in self.usuarios for prestamo in user.libros_prestados if user == usuario):
            self.usuarios.remove(usuario)
            return print("No se puede borrar, debido a que este usuario esta con un libro prestado")
        return False
    
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def borrar_libro(self, libro):
        if not libro.prestado:
            self.libros.remove(libro)
            return print("No se puede borrar el libro, debido a que esta prestado")
        return False
    
    def listar_libros_disponibles_por_categoria(self):
        libros_disponibles = {}
        for libro in self.libros:
            if not libro.prestado:
                if libro.categoria in libros_disponibles:
                    libros_disponibles[libro.categoria].append(libro.titulo)
                else:
                    libros_disponibles[libro.categoria] = [libro.titulo]
        return libros_disponibles
    
    def listar_libros_prestados_por_usuario(self, usuario):        
        libros_prestados = []
        for prestamo in usuario.libros_prestados:
            libros_prestados.append((prestamo[0].titulo, prestamo[1]))
        libros_prestados.sort(key=lambda x: x[1])
        return libros_prestados

biblioteca = Biblioteca()

usuario1 = Usuario("Carlos", "Toro")

libro1 = Libro("Apple", "Tecnologia")

biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_libro(libro1)

usuario1.prestar_libro(libro1, datetime.now())

print("Libros disponibles por categoria: ")
print(biblioteca.listar_libros_disponibles_por_categoria())

print("\nLibros prestados por usuario: ")
print(biblioteca.listar_libros_prestados_por_usuario(usuario1))

print("\nIntentando borrar libro prestado...")
print(biblioteca.borrar_libro(libro1))

print("\nIntentando borrar usuario con libro prestado...")
print(biblioteca.borrar_usuario(usuario1))