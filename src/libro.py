from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, autor, numero_paginas, titulo, ano_publicacion):
        super().__init__(titulo, ano_publicacion)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_numero_paginas(self):
        return self.numero_paginas

    def set_numero_paginas(self, numero_paginas):
        self.numero_paginas = numero_paginas

    def __str__(self):
        return f"Libro{{Titulo={self.titulo}, anoPublicacion={self.ano_publicacion}, Autor={self.autor}, Numero_de_paginas={self.numero_paginas}}}"
