class Publicacion:
    def __init__(self, titulo='', ano_publicacion=0):
        self.titulo = titulo
        self.ano_publicacion = ano_publicacion

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_ano_publicacion(self):
        return self.ano_publicacion

    def set_ano_publicacion(self, ano_publicacion):
        self.ano_publicacion = ano_publicacion

    def __str__(self):
        return f"Publicacion{{Titulo={self.titulo}, anoPublicacion={self.ano_publicacion}}}"
