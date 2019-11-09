import math

class TiposTriangulo():
    def __init__(self, primer_lado, segundo_lado, tercer_lado):
        self.primer_lado  = primer_lado
        self.segundo_lado = segundo_lado
        self.tercer_lado  = tercer_lado

    def ver_tipo_triangulo(self):
        # -- los tres lados son IGUALES
        if self.primer_lado == self.segundo_lado and self.segundo_lado == self.tercer_lado and self.tercer_lado == self.primer_lado:
            return "equilátero"
        else:
            if (self.primer_lado != self.segundo_lado and self.segundo_lado != self.tercer_lado and self.tercer_lado != self.primer_lado):
                return "rectángulo"

        return "isósceles"


    def __repr__(self):
        return f'El triángulo es: {mitriangulo.ver_tipo_triangulo()}'


    #self.primer_lado  = int(input("Escribe la longitud del primer lado: "))
    #self.segundo_lado = int(input("Escribe la longitud del primer lado: "))
    #self.tercer_lado  = int(input("Escribe la longitud del primer lado: "))

#mitriangulo = TiposTriangulo(self.primer_lado, self.segundo_lado, self.tercer_lado)

#mitriangulo = TiposTriangulo(3, 3, 3)

#mitriangulo = TiposTriangulo(3, 7, 3)

mitriangulo = TiposTriangulo(3, 7, 10)

print(mitriangulo)

