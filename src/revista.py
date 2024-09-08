from publicacion import Publicacion

class Revista(Publicacion):
    def __init__(self, numero_revistas, nombre_revista, titulo, ano_publicacion):
        super().__init__(titulo, ano_publicacion)
        self.numero_revistas = numero_revistas
        self.nombre_revista = nombre_revista

    def get_numero_revistas(self):
        return self.numero_revistas

    def set_numero_revistas(self, numero_revistas):
        self.numero_revistas = numero_revistas

    def get_nombre_revista(self):
        return self.nombre_revista

    def set_nombre_revista(self, nombre_revista):
        self.nombre_revista = nombre_revista

    def __str__(self):
        return f"Revista{{Titulo={self.titulo}, anoPublicacion={self.ano_publicacion}, NumeroRevistas={self.numero_revistas}, NombreRevista={self.nombre_revista}}}"
