import math

class TiposTriangulo():
    def __init__(self, primer_lado, segundo_lado, tercer_lado):
        self.primer_lado  = primer_lado
        self.segundo_lado = segundo_lado
        self.tercer_lado  = tercer_lado

    @property
    def ver_tipo_triangulo(self):
        # -- los tres lados son IGUALES
        if self.primer_lado == self.segundo_lado and self.segundo_lado == self.tercer_lado and self.tercer_lado == self.primer_lado:
            return "equilátero"
        else:
            # -- los tres lados son DISTINTOS
            if (self.primer_lado != self.segundo_lado and self.segundo_lado != self.tercer_lado and self.tercer_lado != self.primer_lado):
                return "rectángulo"

        # -- sólo UN lado es DISTINTO
        return "isósceles"

    def __repr__(self):
        return f'El primer lado vale: {self.primer_lado} - El segundo lado vale {self.segundo_lado}\
  - El tercer lado vale: {self.tercer_lado} ==> El triángulo es: {mitriangulo.ver_tipo_triangulo}'


# ----
primer_lado  = int(input("Escribe la longitud del primer lado: "))
segundo_lado = int(input("Escribe la longitud del primer lado: "))
tercer_lado  = int(input("Escribe la longitud del primer lado: "))

mitriangulo = TiposTriangulo(primer_lado, segundo_lado, tercer_lado)

print(mitriangulo)


