from src.Muestra import Muestra
import csv


class Banco():

    def __init__(self):
        self.__variasMuestras = []
        self.__sangreRecolectada = {
            "A+": 0, "B+": 0, "AB+": 0, "O+": 0, "A-": 0, "B-": 0, "AB-": 0, "O-": 0}

    def leer_datos(self):
        # abre el archivo sangre.csv, lee la información de este, crea instancias de muestra y las almacena.
        with open('./csv/sangre.csv') as File:
            reader = csv.DictReader(File,delimiter=';')
            for row in reader:
                self.__variasMuestras.append(row)
                muestra = Muestra(row)
                tipoSangre = muestra.tipo_sangre()
                self.__sangreRecolectada[tipoSangre] += float(
                    muestra.getCantidad())

    def mostrar(self):
        # muestra, para cada tipo de sangre, la cantidad de sangre total recolectada, en Litros.
        print("Sangre Recolectada")
        for tipo in self.__sangreRecolectada:
            # convertir a litros y redondeo a 2 decimales
            litros = str(round(self.__sangreRecolectada[tipo]/1000, 2))
            print(tipo+" : "+litros+" L")
