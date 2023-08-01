
"""Archivo que contiene la ejecucion principal del programa"""

from method import *
import time


if __name__ == '__main__':                            #aqui se comienza a ejecutar

    tiempo_inicial = time.time()

    VAR_TEMP = "00:59:59"
    sol_th = 0.65
    flag_first_time = 1
    ID_tracking = 0
    data_stage1 = {}
    while True:
        ID_tracking += 1
        data_stage1 = make_validation_propio(VAR_TEMP, flag_first_time, data_stage1)
        data_stage2 = make_verification_model(sol_th, False, VAR_TEMP)
        create_csv_AG(data_stage2, flag_first_time, ID_tracking)
        str_temp = make_temp(tiempo_inicial, time.time(), show=False)
        print("ID: {}  Tiempo total transcurrido: {}" .format(ID_tracking, str_temp))
        flag_first_time = 0
