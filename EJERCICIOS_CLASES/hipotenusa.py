import math

class TrianguloRectangulo():
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    @property
    def calculo_hipotenusa(self):
        hipotenusa = math.sqrt(self.cateto1*self.cateto1 + self.cateto2*self.cateto2)
        hipotenusa = round(hipotenusa, 2)
        return hipotenusa

    #self._calculo_hipotenusa

    def __repr__(self):
        return f'El cateto primero es: {self.cateto1}. El segundo cateto es: {self.cateto2} ==> La hipotenusa vale: {self.calculo_hipotenusa}'


mitriangulo = TrianguloRectangulo(4, 7)

print(mitriangulo.calculo_hipotenusa)

print(mitriangulo)

