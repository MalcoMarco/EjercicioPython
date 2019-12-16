class Muestra():
    # constructor
    def __init__(self, muestra):
        # inicializar los atributos de la clase.
        self.__AntiA = int(muestra["AntiA"])
        self.__AntiB = int(muestra["AntiB"])
        self.__AntiRh = muestra["AntiRh"]
        self.__Cantidad = muestra["Cantidad"]
        self.variable = 5

    def __tipo_ABO(self):
        # calcula y retorna el tipo ABO de la muestra (ej: B).
        if self.__AntiA == 0 and self.__AntiB == 0:
            return "O"

        if self.__AntiA == 0 and self.__AntiB == 1:
            return "B"

        if self.__AntiA == 1 and self.__AntiB == 0:
            return "A"

        if self.__AntiA == 1 and self.__AntiB == 1:
            return "AB"

    def __tipo_Rh(self):
        # calcula y retorna el tipo Rh de la muestra (ej: +).
        if self.__AntiRh[0] == "D":
            return "+"
        if self.__AntiRh[0] == "d":
            return "-"

    def tipo_sangre(self):
        # calcula y retorna el tipo de sangre de la muestra ej: B+.
        # obtener el tipo ABO
        Abo = self.__tipo_ABO()
        # obtener tipo rh
        Rh = self.__tipo_Rh()
        return Abo+Rh

    def getCantidad(self):
        return self.__Cantidad
