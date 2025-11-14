# Creamos libros
class Libro:
    def __init__(self, titulo, disponible=True):
        self.titulo = titulo
        self.disponible = disponible


# Creamos Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libro_prestado = []


# Bliblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo):
        self.libros[titulo] = Libro(titulo)

    def registrar_usuarios(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)

    def prestar_libro(self, titulo_libro, nombre_usuario):
        if titulo_libro not in self.libros:
            raise Exception("Libro no encontrado")
        if nombre_usuario not in self.usuarios:
            raise Exception("Usuario no registrado")

        libro = self.libros[titulo_libro]
        usuarios = self.usuarios[nombre_usuario]

        if not libro.disponible:
            raise Exception("Libro no Disponible")

        libro.disponible = False
        usuarios.libros_prestado.append(titulo_libro)
        return True
