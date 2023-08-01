
"""archivo que contiene las funciones de ejecucion"""

import os
import random
import newsegmentation as ns
from myseg import Segmentation_60
from tabulate import tabulate
from time import time
import math
import pygad as pg
import pandas as pd

lista_validacion = []
cont_list_val = 0
initial_flag = True
val_progress = 0
cont_generation = 0         #ojo estaba a -1
tot = 0
cont_file = 0
tiempo_estimado = 0


def make_txt_5():
    """funcion que estipula los argumentos de entrada para realizar la base de datos con la premisa de 5 minutos"""
    t_inicial = time()
    VAR_TEMP="00:05:00"
    outpath=r'VTT\txt_gt\5mins\txt'
    make_txt(VAR_TEMP, outpath)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_txt_60():
    """funcion que estipula los argumentas de entrada para realizar la base de datos con la premisa de 60 minutos"""
    t_inicial = time()
    VAR_TEMP="00:59:59"
    outpath = r'VTT\txt_gt\60mins\txt'
    make_txt(VAR_TEMP, outpath)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_5():
    """funcion que estipula los argumentos de entrada para realizar la segmentacion para los 5 primeros minutos de TD"""
    t_inicial = time()
    VAR_TEMP = "00:05:00"
    make_segmentation(VAR_TEMP, True, False, False, False)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_60():
    """funcion que estipula los argumentos de entrada para realizar la segmentacion para los 60 minutos del TD"""
    t_inicial = time()
    VAR_TEMP = "00:59:59"
    make_segmentation(VAR_TEMP, True, False, False, False, True)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_60_ev_onebd():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de un TD"""
    t_inicial = time()
    VAR_TEMP = "00:59:59"
    make_segmentation(VAR_TEMP, False, True, False, False)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_5_ev_onebd():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de un TD"""
    t_inicial = time()
    VAR_TEMP = "00:05:00"
    make_segmentation(VAR_TEMP, False, True, False, False, False)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_5_ev_onebd_p():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de un TD"""
    t_inicial = time()
    VAR_TEMP = "00:05:00"
    make_segmentation(VAR_TEMP, False, True, False, False, True)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_60_ev_onebd_p():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de un TD"""
    t_inicial = time()
    VAR_TEMP = "00:59:59"
    make_segmentation(VAR_TEMP, False, True, False, False, True)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_60_ev_allbd():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de los TD en un directorio"""
    t_inicial = time()
    VAR_TEMP = "00:59:59"
    make_segmentation(VAR_TEMP, False, True, True, True, False)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_60_ev_allbd_p():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de los TD en un directorio"""
    t_inicial = time()
    VAR_TEMP = "00:59:59"
    make_segmentation(VAR_TEMP, False, True, True, True, True)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_5_ev_allbd():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de los TD en un directorio"""
    t_inicial = time()
    VAR_TEMP = "00:05:00"
    make_segmentation(VAR_TEMP, False, True, True, True, False)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_segmentation_5_ev_allbd_p():
    """funcion que estipula los argumentos de entrada para realizar la evaluacion del modelo para 60 minutos de los TD en un directorio"""
    t_inicial = time()
    VAR_TEMP = "00:05:00"
    make_segmentation(VAR_TEMP, False, True, True, True, True)
    t_final = time()
    make_temp(t_inicial, t_final, True)


def make_validation_5_comun():
    VAR_TEMP = "00:05:00"
    data = make_validation_comun(VAR_TEMP)
    print(data)


def make_validation_5_propio():
    VAR_TEMP = "00:05:00"
    data = make_validation_propio(VAR_TEMP)
    print(data)


def make_validation_60_comun():
    VAR_TEMP = "00:59:59"
    data = make_validation_comun(VAR_TEMP)
    print(data)


def make_validation_60_propio():
    VAR_TEMP = "00:59:59"
    data = make_validation_propio(VAR_TEMP)
    print(data)


def make_verificacion_model_restric_5():
    sol_th = 0.65
    time_limit = "00:05:00"
    make_verification_model(sol_th, True, time_limit)


def make_verificacion_model_restric_60():
    sol_th = 0.65
    time_limit = "00:59:59"
    make_verification_model(sol_th, True, time_limit)


def make_verificacion_model_permis_5():
    sol_th = 0.65
    time_limit = "00:05:00"
    make_verification_model(sol_th, False, time_limit)


def make_verificacion_model_permis_60():
    sol_th = 0.65
    time_limit = "00:59:59"
    make_verification_model(sol_th, False, time_limit)


def make_txt(time_limit, MY_TXT_PATH):
    """funcion que unicamente transforma la base de datos de .vtt a .txt
    inputs: -> time_limit: tiempo limite de conversion
            -> MY_TXT_PATH: zona donde se almacenaran los archivo txt"""

    PATH_BASE_VTT = r'VTT\vtt_files\vtt_files'

    total_count_vtt = 0
    count_vtt = 0
                                                                                 # contamos cuantos archivos vtt hay para llevar la cuenta y ofrecer un porcentaje de conversion

    for first_level in os.listdir(PATH_BASE_VTT):
        if len(first_level.split('.')) == 1:
                                                                                 # si tiene 1 de tamaño es que no tiene extension y es un directorio, continuamos
            for second_level in os.listdir(PATH_BASE_VTT + "\\" + first_level):
                if ".vtt" in second_level:
                    total_count_vtt = total_count_vtt + 1

                                                                                 # count_vtt contiene el numero total de .vtt a convertir

    for dir_name in os.listdir(PATH_BASE_VTT):

        for news_name in os.listdir(PATH_BASE_VTT + "\\" + dir_name):

            path = PATH_BASE_VTT + "\\" + dir_name + "\\" + news_name           #path donde se encuentra el archivo .vtt, de aqui obtendremos nombre_de_noticia/numero_de_noticiero para guardar los txt resultantes
            data_path = path.split("\\")                                        # separamos el path en una lista segun los \ del path
            directory_news = data_path[-2]                                      # obtenemos el nombre de la carpeta donde se va a guardar
            number_news = data_path[-1]                                         # obtenemos el numero de noticia, pero el numero sale con la extension de vtt
            number_news = number_news.split(".")                                # separamos entre informacion y extension
            number_news = number_news[0] + ".txt"                               # concatenamos informacion (numero de noticia) con . txt
            out_txt_path = MY_TXT_PATH + "\\" + directory_news + "\\" + number_news  # ya tenemos toda la informacion para construir el path de guardado

            ns.default_dbt(path, out_txt_path, time_limit)                      #llamamos a la funcion encargada de realizar la escritura

            count_vtt = count_vtt + 1                                           #cuenta de progreso
            vtt_percent = (count_vtt / total_count_vtt) * 100
            if os.name == "nt":                                                 #borrado de pantalla segun OS
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")
            print("{:.2f} %".format(vtt_percent))


def make_segmentation(time_limit, show=True, evaluate=False, allbd=False, save_csv=False, custom_params=False):
    """funcion que realiza el recorrido completo de la segmentacion (simulacion real) para los minutos indicados
    inputs: -> time_limit: indica el tiempo que se va a leer de los vtt para realizar la segmentacion
            -> show: var de activacion (True o False) indica si se muestran las matrices R por pantalla
            -> evaluate: var de activacion (True o False) indica si se realiza la evaluacion despues de la segmentacion
            -> allbd: var de activacion (True o False) indica si se realiza la evaluacion de toda la carpeta propuesta
            -> save_csv: var de activacion (True o False) indica si se almacenan en un csv los datos obtenidos
            -> custom_params: var de activacion (True o False) indica si se van a introducir los parametros a mano o se
            van a utilizar los parametros por defecto
    """

    FBBCM_th_p = -1
    CB_th_p = -1
    OIM_p = -1
    PBMM_th_p = -1
    w_p = -1
    var_p = -1
    betta_p = -1
    tiempo_estimado = 0
    count_vtt = 0
    count_progress = 0
    path_seg = ""
    comprobante = ""
    flag_muestra = False
    flag_cabecera = False

    if not allbd:                                                                   #si allbd es false, entonces solo queremos segmentar un archivo vtt
        while comprobante != "vtt" and comprobante != "txt":                        #mientras que la extension del archivo no sea txt o vtt, seguimos pidiendo la direccion correcta
            path_seg = input("introduce la direccion del archivo a segmentar: ")    #pedimos la direccion del archivo a segmentar
            comprobante = path_seg.split('.')                                       #separamos el path entre direccion y extension
            comprobante = comprobante[-1]                                           #guardamos la extension que nos sirve para realizar la comprobacion del while

        if evaluate:
            #comprobar aqui si existe su archivo gt
            path_base = "VTT\\"
            path_ev = ""
            split_path = path_seg.split('\\')                                                                           # separamos en \ el path de entrada para conseguir el path de salida a partir de este
            num_path = split_path[-1]                                                                                   # obtenemos el numero.txt
            num_path = num_path.split('.')                                                                              # separamos por el punto
            num_path = num_path[0]                                                                                      # nos quedamos con el numero
            name_path = split_path[-2]                                                                                  # nos quedamos con el nombre de las noticias
            if time_limit == "00:05:00":                                                                                # si la evaluacion es para 5 minutos
                path_ev = path_base + "txt_gt\\5mins\\gt\\" + name_path + "\\" + num_path + ".txt"                      # este es el path donde se encuentra el ground truth
            elif time_limit == "00:59:59":                                                                              # si la evaluacion es para 60 minutos
                path_ev = path_base + "txt_gt\\60mins\\gt\\" + name_path + "\\" + num_path + ".txt"                     # este es el path donde se encuentra su ground truth
            if not os.path.exists(path_ev):
                print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
                return -1
        if not custom_params:
            myNews = Segmentation_60(path_seg, time_limit)                              # objeto que indica el numero de noticias segmentadas
        else:
            while betta_p < 0 or betta_p > 1:
                print("\nIntroduce los parametros segun se van indicando: ")
                betta_p = float(input("BETTA (valor decimal entre 0 y 1): "))
            while var_p < 0 or var_p > 1:
                var_p = float(input("var_p (valor decimal entre 0 y 1): "))
            while w_p < 0 or w_p > 1:
                w_p = float(input("w_p (valor decimal entre 0 y 1): "))
            while PBMM_th_p < 0 or PBMM_th_p > 1:
                PBMM_th_p = float(input("PBMM_th_p (valor decimal entre 0 y 1): "))
            while OIM_p < 0:
                OIM_p = float(input("OIM_p (valor entero positivo): "))
            while CB_th_p < 0 or CB_th_p > 1:
                CB_th_p = float(input("CB_th_p (valor decimal entre 0 y 1): "))
            while FBBCM_th_p < 0 or FBBCM_th_p > 1:
                FBBCM_th_p = float(input("FBBCM_th_p (valor decimal entre 0 y 1): "))

            myNews = Segmentation_60(path_seg, time_limit, betta_p, (var_p, w_p), (PBMM_th_p, OIM_p, CB_th_p), (FBBCM_th_p,) )  # objeto que indica el numero de noticias segmentadas

        muestra_hiperparametros(myNews)                                             #mostramos los hiperparametros actuales
        print("\n\n\n")
        if show:                                                                    # si show es true mostramos los plot
            for pieceOfNews in myNews:                                              # hacemos plot de cada una de las noticias segmentadas
                print(pieceOfNews)
                myNews.plotmtx()
        if evaluate:                                                                #si la evaluacion esta activada
            performance = make_evaluate(myNews, path_seg, time_limit, True)
            if save_csv:
                if save_csv and performance != -1:                                                                      # si activo el guardado
                    make_csv(performance, os.path.dirname(path_seg), path_seg.split('\\')[-1], flag_cabecera)
            return performance
    else:                                                                                                               # si allbd es true, entonces queremos segmentar todos los .vtt que haya en cierto directorio
        paths_dir = input("introduce la direccion del directorio donde se encuentran los archivos .vtt o .txt a evaluar: ")
        while not os.path.exists(paths_dir):                                                                            #esperamos a una entrada de una carpeta que exista
            print("No existe la direccion suministrada")
            paths_dir = input("introduce la direccion del directorio donde se encuentran los archivos .vtt o .txt a evaluar: ")

        for file_text in os.listdir(paths_dir):                                                                         #en este bloque realizamos la cuenta del numero total de vtt files hay
            if os.path.isdir(paths_dir + "\\" + file_text):                                                             #sirve para marcar el % de avance de la evaluacion
                count_vtt += len(os.listdir(paths_dir + "\\" + file_text))
            else:
                count_vtt = len(os.listdir(paths_dir))                                                                  #count_vtt contiene el numero total de archivos vtt

        for file_text in os.listdir(paths_dir):                                                                         #recorremos los archivos que hay en dicha carpeta
            if os.path.isdir(paths_dir + "\\" + file_text):                                                             #si es un directorio
                for file_text_in in os.listdir(paths_dir + "\\" + file_text):                                           #recorremos otra vez los archivos de dicha carpeta
                    tiempo_estimado_inicial = time()

                    if evaluate:                                                                                        #si vamos a realizar la evaluacion
                                                                                                                        # comprobar aqui si existe su archivo gt
                        path_base = "VTT\\"
                        path_ev = ""
                        path_tot = paths_dir + "\\" + file_text + "\\" + file_text_in
                        split_path = path_tot.split('\\')                                                               # separamos en \ el path de entrada para conseguir el path de salida a partir de este
                        num_path = split_path[-1]                                                                       # obtenemos el numero.txt
                        num_path = num_path.split('.')                                                                  # separamos por el punto
                        num_path = num_path[0]                                                                          # nos quedamos con el numero
                        name_path = split_path[-2]                                                                      # nos quedamos con el nombre de las noticias
                        if time_limit == "00:05:00":                                                                    # si la evaluacion es para 5 minutos
                            path_ev = path_base + "txt_gt\\5mins\\gt\\" + name_path + "\\" + num_path + ".txt"          # este es el path donde se encuentra el ground truth
                        elif time_limit == "00:59:59":                                                                  # si la evaluacion es para 60 minutos
                            path_ev = path_base + "txt_gt\\60mins\\gt\\" + name_path + "\\" + num_path + ".txt"         # este es el path donde se encuentra su ground truth
                        if not os.path.exists(path_ev):
                            print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
                            continue

                    if not custom_params:
                        myNews = Segmentation_60(paths_dir + '\\' + file_text + '\\' + file_text_in, time_limit)  # objeto que indica el numero de noticias segmentadas
                    else:
                        while betta_p < 0 or betta_p > 1:
                            print("\nIntroduce los parametros segun se van indicando: ")
                            betta_p = float(input("BETTA (valor decimal entre 0 y 1): "))
                        while var_p < 0 or var_p > 1:
                            var_p = float(input("var_p (valor decimal entre 0 y 1): "))
                        while w_p < 0 or w_p > 1:
                            w_p = float(input("w_p (valor decimal entre 0 y 1): "))
                        while PBMM_th_p < 0 or PBMM_th_p > 1:
                            PBMM_th_p = float(input("PBMM_th_p (valor decimal entre 0 y 1): "))
                        while OIM_p < 0:
                            OIM_p = float(input("OIM_p (valor entero positivo): "))
                        while CB_th_p < 0 or CB_th_p > 1:
                            CB_th_p = float(input("CB_th_p (valor decimal entre 0 y 1): "))
                        while FBBCM_th_p < 0 or FBBCM_th_p > 1:
                            FBBCM_th_p = float(input("FBBCM_th_p (valor decimal entre 0 y 1): "))

                        myNews = Segmentation_60(paths_dir + '\\' + file_text + '\\' + file_text_in, time_limit,
                                                 betta_p, (var_p, w_p), (PBMM_th_p, OIM_p, CB_th_p),
                                                 (FBBCM_th_p,))  # objeto que indica el numero de noticias segmentadas

                    if not flag_muestra:                                                                                # la primera vez mostramos los hiperparametros actuales
                        muestra_hiperparametros(myNews)
                        flag_muestra = True

                    if evaluate:                                                                                        # si la evaluacion esta activa
                        performance = make_evaluate(myNews, paths_dir + '\\' + file_text + '\\' + file_text_in, time_limit, False)                   # llamamos a la funcion de evaluacion
                        if save_csv and performance != -1:                                                              # si activo el guardado
                            flag_cabecera = make_csv(performance, paths_dir + '\\' + file_text, file_text_in, flag_cabecera)

                    if show:                                                                                            #si show activo mostramos las matrices R de cada noticia segmentada
                        for pieceOfNews in myNews:
                            print(pieceOfNews)
                            myNews.plotmtx()
                    count_progress += 1                                                                                 #sumamos uno a la cuenta de porcentaje
                    percent_progress = (count_progress / count_vtt) * 100
                    print("{:.2f} % completado" .format(percent_progress))
                    tiempo_estimado_final = time()
                    tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial                             # segundos que tarda en evaluarse un archivo
                    tiempo_estimado += tiempo_actual_archivo                                                            # sumamos todos los datos de tiempos
                    tiempo_estimado_medio = tiempo_estimado / count_progress                                            # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
                    tiempo_estimado_out = tiempo_estimado_medio * (count_vtt - count_progress)                          # tiempo estimado para finalizar en segundos
                    print("Tiempo estimado de finalizacion a partir de este momento: {}\n".format(
                        make_temp(0, tiempo_estimado_out, False)))
            else:                                                                                                       #en este caso los archivos se encuentran directamente en esta carpeta
                tiempo_estimado_inicial = time()

                if evaluate:                                                                                            #si vamos a realizar la evaluacion
                                                                                                                        # comprobar aqui si existe su archivo gt
                    path_base = "VTT\\"
                    path_ev = ""
                    path_tot = paths_dir + "\\" + file_text
                    split_path = path_tot.split('\\')                                                                   # separamos en \ el path de entrada para conseguir el path de salida a partir de este
                    num_path = split_path[-1]                                                                           # obtenemos el numero.txt
                    num_path = num_path.split('.')                                                                      # separamos por el punto
                    num_path = num_path[0]                                                                              # nos quedamos con el numero
                    name_path = split_path[-2]                                                                          # nos quedamos con el nombre de las noticias
                    if time_limit == "00:05:00":                                                                        # si la evaluacion es para 5 minutos
                        path_ev = path_base + "txt_gt\\5mins\\gt\\" + name_path + "\\" + num_path + ".txt"              # este es el path donde se encuentra el ground truth
                    elif time_limit == "00:59:59":                                                                      # si la evaluacion es para 60 minutos
                        path_ev = path_base + "txt_gt\\60mins\\gt\\" + name_path + "\\" + num_path + ".txt"             # este es el path donde se encuentra su ground truth
                    if not os.path.exists(path_ev):
                        print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
                        continue

                    if not custom_params:
                        myNews = Segmentation_60(paths_dir + '\\' + file_text, time_limit)  # objeto que indica el numero de noticias segmentadas
                    else:
                        while betta_p < 0 or betta_p > 1:
                            print("\nIntroduce los parametros segun se van indicando: ")
                            betta_p = float(input("BETTA (valor decimal entre 0 y 1): "))
                        while var_p < 0 or var_p > 1:
                            var_p = float(input("var_p (valor decimal entre 0 y 1): "))
                        while w_p < 0 or w_p > 1:
                            w_p = float(input("w_p (valor decimal entre 0 y 1): "))
                        while PBMM_th_p < 0 or PBMM_th_p > 1:
                            PBMM_th_p = float(input("PBMM_th_p (valor decimal entre 0 y 1): "))
                        while OIM_p < 0:
                            OIM_p = float(input("OIM_p (valor entero positivo): "))
                        while CB_th_p < 0 or CB_th_p > 1:
                            CB_th_p = float(input("CB_th_p (valor decimal entre 0 y 1): "))
                        while FBBCM_th_p < 0 or FBBCM_th_p > 1:
                            FBBCM_th_p = float(input("FBBCM_th_p (valor decimal entre 0 y 1): "))

                        myNews = Segmentation_60(paths_dir + '\\' + file_text, time_limit,
                                                 betta_p, (var_p, w_p), (PBMM_th_p, OIM_p, CB_th_p),
                                                 (FBBCM_th_p,))  # objeto que indica el numero de noticias segmentadas

                if not flag_muestra:                                                        #la primera vez mostramos los hiperparametros actuales
                    try:
                        muestra_hiperparametros(myNews)
                    except:
                        pass
                    flag_muestra = True
                if show:                                                                    #si show activo mostramos las matrices R de cada noticia segmentada
                    for pieceOfNews in myNews:
                        print(pieceOfNews)
                        myNews.plotmtx()

                if evaluate:                                                                                    #si la evaluacion esta activa
                    performance = make_evaluate(myNews, paths_dir + '\\' + file_text, time_limit, False)        #llamamos a la funcion de evaluacion
                    if save_csv and performance != -1:                                                          #si activo el guardado
                        flag_cabecera = make_csv(performance, paths_dir, file_text, flag_cabecera)

                count_progress += 1                                                                                     #sumamos uno a la cuenta de porcentaje
                percent_progress = (count_progress / count_vtt) * 100
                print("{:.2f} % completado" .format(percent_progress))
                tiempo_estimado_final = time()
                tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial                                 #segundos que tarda en evaluarse un archivo
                tiempo_estimado += tiempo_actual_archivo                                                                #sumamos todos los datos de tiempos
                tiempo_estimado_medio = tiempo_estimado / count_progress                                                #dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
                tiempo_estimado_out = tiempo_estimado_medio * (count_vtt - count_progress)                              #tiempo estimado para finalizar en segundos
                print("Tiempo estimado de finalizacion a partir de este momento: {}\n" .format(make_temp(0,tiempo_estimado_out,False)))


def make_evaluate(myNews, path_seg, time_limit, show):

    """funcion que evalua las noticias segmentadas y calcula las medidas de rendimiento
    inputs: -> myNews: objeto de tipo newSegmentation con la segmentacion realizada
            -> path_seg: direccion donde se encuentra el archivo a evaluar
            -> time_limit: tiempo limite de conversion de los vtt (5 minutos o una hora)
            -> show: var de activacion (True o False) para mostrar por consola los datos obtenidos en rendimiento
    outputs: -> performance: tupla con los datos de rendimientos"""

    path_base = "VTT\\"
    path_ev = ""
    split_path = path_seg.split('\\')                                               # separamos en \ el path de entrada para conseguir el path de salida a partir de este
    num_path = split_path[-1]                                                       # obtenemos el numero.txt
    num_path = num_path.split('.')                                                  # separamos por el punto
    num_path = num_path[0]                                                          # nos quedamos con el numero
    name_path = split_path[-2]                                                      # nos quedamos con el nombre de las noticias
    if time_limit == "00:05:00":                                                    # si la evaluacion es para 5 minutos
        path_ev = path_base + "txt_gt\\5mins\\gt\\" + name_path + "\\" + num_path + ".txt"              # este es el path donde se encuentra el ground truth
    elif time_limit == "00:59:59":                                                                      # si la evaluacion es para 60 minutos
        path_ev = path_base + "txt_gt\\60mins\\gt\\" + name_path + "\\" + num_path + ".txt"             # este es el path donde se encuentra su ground truth
    try:
        performance = myNews.evaluate(path_ev, False, True)                                                  # evaluamos y almacenamos en performance los valores de los rendimientos
    except FileNotFoundError:
        print("no se ha encontrado el archivo gt de {} para el tiempo {}" .format(name_path, time_limit))
        return -1
    except ValueError:
        print("Ha ocurrido una excepcion de integridad en {}, repasar el gt con la frase indicada" .format(path_ev))
        return -1

    if show:
        performance_table = [['Precision', performance['Precision']],                                       # preparamos la tabla de resultados en el rendimiento
                            ['Recall', performance['Recall']],
                            ['F1', performance['F1']],
                            ['WD', performance['WD']],
                            ['Pk', performance['Pk']]]

        print('\n\n\n|||||||||||| VALORES DE LA EVALUACION ||||||||||||||\n\n\n')
        print(tabulate(performance_table, tablefmt="grid"))

    return performance


def muestra_hiperparametros(myNews):

    """funcion que muestra los hiperparametros actuales del modelo
    inputs: -> myNews: objeto de segmentacion
    """

    hiperparameters_table = [['Betta (TDM Decorrelator)', myNews.parameters['betta_tdm']],              # preparamos la tabla de hiperparametros usados en la segmentacion para mostrarla
                             ['varianza (GPA preSDM Gaussian)', myNews.parameters['gpa'][0]],
                             ['w (GPA preSDM Gaussian Weight)', myNews.parameters['gpa'][1]],
                             ['PBMM-th (SDM PBMM threshold)', myNews.parameters['sdm'][0]],
                             ['OIM (SDM fail oportunities)', myNews.parameters['sdm'][1]],
                             ['CB-th (SDM checkback threshold)', myNews.parameters['sdm'][2]],
                             ['FBBCM-th (LCM FBBCM-threshold)', myNews.parameters['lcm'][0]]]

    print('\n\n\n|||||||||||| HIPERPARAMETROS DE LA SEGMENTACION ||||||||||||||\n\n\n')                 # mostramos los resultados
    print(tabulate(hiperparameters_table, tablefmt="grid"))


def make_csv(performance, paths_dir, file_text, flag_cabecera):

    """funcion que almacena los datos de las evaluaciones en un archivo csv
    inputs: -> performance: tupla con los datos del rendimiento
            -> paths_dir: direccion donde el ultimo elemento es la carpeta que contiene los vtt
            -> file_text: numero de noticiero y extension
            -> flag_cabecera: flag que indica si es la primera vez que se accede al archivo csv
    outputs: ->flag_cabecera: devolvemos el estado del flag"""

    if not flag_cabecera:
        try:
            os.remove("performance.csv")                                                            #intentamos eliminar el archivo la primera vez para evitar duplicados
        except:
            pass

    with open("performance.csv", "a") as temporalEv:                                                # abrimos un archivo csv
        if not flag_cabecera:
            temporalEv.writelines('Noticia_principal,Numero_TD,Precision,Recall,F1,WD,Pk\n')                          # agregamos las cabeceras la primera vez
            flag_cabecera = True
        temporalEv.writelines("{},{},{},{},{},{},{}\n".format(paths_dir.split('\\')[-1], file_text, # agregamos en cada vuelta los valores del rendimiento
                                                                  performance['Precision'],
                                                                  performance['Recall'],
                                                                  performance['F1'],
                                                                  performance['WD'],
                                                                  performance['Pk']))
        return flag_cabecera


def make_csv_val(performance, paths_dir, file_text, flag_cabecera):

    """funcion que almacena los datos de las validaciones en un archivo csv
    inputs: -> performance: tupla con los datos del rendimiento
            -> paths_dir: direccion donde el ultimo elemento es la carpeta que contiene los vtt
            -> file_text: numero de noticiero y extension
            -> flag_cabecera: flag que indica si es la primera vez que se accede al archivo csv
    outputs: ->flag_cabecera: devolvemos el estado del flag"""

    if not flag_cabecera:
        try:
            os.remove("validation.csv")                                                            #intentamos eliminar el archivo la primera vez para evitar duplicados
        except:
            pass

    with open("validation.csv", "a") as temporalEv:                                                # abrimos un archivo csv
        if not flag_cabecera:
            temporalEv.writelines('Noticia_principal,Numero_TD,Precision,Recall,F1,WD,Pk\n')                          # agregamos las cabeceras la primera vez
            flag_cabecera = True
        temporalEv.writelines("{},{},{},{},{},{},{}\n".format(paths_dir.split('\\')[-1], file_text, # agregamos en cada vuelta los valores del rendimiento
                                                                  performance['Precision'],
                                                                  performance['Recall'],
                                                                  performance['F1'],
                                                                  performance['WD'],
                                                                  performance['Pk']))
        return flag_cabecera


def make_temp(inicio, final, show=True):

    """funcion que obtiene el tiempo en segundos inicial y final y convierte al formato dias horas minutos segundos
    para tener control del tiempo de ejecucion
    inputs: -> inicio: segundos de partida
            -> final: segundos de finalizacion
            -> show: si esta activo, muestra por pantalla el tiempo calculado
    outputs: -> string con formato XX dias :: XX horas :: XX minutos :: XX segundos con el tiempo transcurrido"""

    t_seg = final - inicio
    t_min = 0
    t_hor = 0
    t_dia = 0
    if t_seg >= 60:
        t_min += math.trunc(t_seg / 60)
        t_seg = t_seg % 60
    if t_min >= 60:
        t_hor += math.trunc(t_min / 60)
        t_min = t_min % 60
    if t_hor >= 24:
        t_dia += math.trunc(t_hor / 24)
        t_hor = t_hor % 24
    if show:
        print("\n\nTiempo de ejecucion -> {:.0f} dias {:2.0f} horas {:2.0f} minutos {:2.0f} segundos".format(t_dia, t_hor, t_min, t_seg))

    return "{:.0f} dias :: {:2.0f} horas :: {:2.0f} minutos :: {:2.0f} segundos" .format(t_dia, t_hor, t_min, t_seg)


def fitness_func_60_propio(solution, solution_idx):
    global initial_flag

    # aqui hacemos la segmentacion y la evaluacion

    # introduccion del archivo

    path_seg = lista_validacion[cont_list_val]

    #for path_seg in lista_validacion:

    # comprobamos si existe el archivo gt

    path_base = "VTT\\"
    split_path = path_seg.split('\\')                                                       # separamos en \ el path de entrada para conseguir el path de salida a partir de este
    num_path = split_path[-1]                                                               # obtenemos el numero.txt
    num_path = num_path.split('.')                                                          # separamos por el punto
    num_path = num_path[0]                                                                  # nos quedamos con el numero
    name_path = split_path[-2]                                                              # nos quedamos con el nombre de las noticias
    path_ev = path_base + "txt_gt\\60mins\\gt\\" + name_path + "\\" + num_path + ".txt"      # este es el path donde se encuentra el ground truth
    if not os.path.exists(path_ev):
        print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
        return 0

    # realizamos la segmentacion

    myNews = Segmentation_60(path_seg, "00:59:59", solution[0], (solution[1], solution[2]),
                             (solution[3], solution[4], solution[5]),
                             (solution[6],))                                                # creamos la segmentacion con los hiperparametros obtenidos en solution

    # evaluamos

    performance = make_evaluate(myNews, path_seg, "00:59:59", False)

    # pasamos los datos de evaluacion por el algoritmo de fitness

    new_fitness = algoritmo_fitness(performance)

    #guardamos los datos en un csv

    if cont_list_val == 0 and initial_flag == True:
        try:
            os.remove("hist_validation.csv")                                                            #intentamos eliminar el archivo la primera vez para evitar duplicados
        except:
            pass

    with open("hist_validation.csv", "a") as temporalEv:                                                # abrimos un archivo csv
        if cont_list_val == 0 and initial_flag == True:
            temporalEv.writelines('Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')                          # agregamos las cabeceras la primera vez
            initial_flag = False
        temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(path_seg.split('\\')[-2],
                                                                  path_seg.split('\\')[-1],                             # agregamos en cada vuelta los valores del rendimiento
                                                                  solution[0],
                                                                  solution[1],
                                                                  solution[2],
                                                                  solution[3],
                                                                  solution[4],
                                                                  solution[5],
                                                                  solution[6],
                                                                  performance['Precision'],
                                                                  performance['Recall'],
                                                                  performance['F1'],
                                                                  performance['WD'],
                                                                  performance['Pk'],
                                                                  new_fitness))


    #hacer un promedio de los resultados obtenidos de cada uno de los archivos

    return new_fitness


def fitness_func_5_propio(solution, solution_idx):
    # aqui hacemos la segmentacion y la evaluacion

    global initial_flag

    #introduccion del archivo

    path_seg = lista_validacion[cont_list_val]

    #comprobamos si existe el archivo gt

    path_base = "VTT\\"
    split_path = path_seg.split('\\')                                                               # separamos en \ el path de entrada para conseguir el path de salida a partir de este
    num_path = split_path[-1]                                                                       # obtenemos el numero.txt
    num_path = num_path.split('.')                                                                  # separamos por el punto
    num_path = num_path[0]                                                                          # nos quedamos con el numero
    name_path = split_path[-2]                                                                      # nos quedamos con el nombre de las noticias
    path_ev = path_base + "txt_gt\\5mins\\gt\\" + name_path + "\\" + num_path + ".txt"              # este es el path donde se encuentra el ground truth
    if not os.path.exists(path_ev):
        print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
        return 0

    #realizamos la segmentacion

    myNews = Segmentation_60(path_seg, "00:05:00", solution[0], (solution[1], solution[2]), (solution[3], solution[4], solution[5]), (solution[6],))         #creamos la segmentacion con los hiperparametros obtenidos en solution

    #evaluamos

    performance = make_evaluate(myNews, path_seg, "00:05:00", False)

    #pasamos los datos de evaluacion por el algoritmo de fitness

    new_fitness = algoritmo_fitness(performance)

    #guardamos los datos en un csv

    if cont_list_val == 0 and initial_flag == True:
        try:
            os.remove("hist_validation.csv")                                                            #intentamos eliminar el archivo la primera vez para evitar duplicados
        except:
            pass

    with open("hist_validation.csv", "a") as temporalEv:                                                # abrimos un archivo csv
        if cont_list_val == 0 and initial_flag == True:
            temporalEv.writelines('Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')                          # agregamos las cabeceras la primera vez
            initial_flag = False
        temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(path_seg.split('\\')[-2],
                                                                  path_seg.split('\\')[-1],                             # agregamos en cada vuelta los valores del rendimiento
                                                                  solution[0],
                                                                  solution[1],
                                                                  solution[2],
                                                                  solution[3],
                                                                  solution[4],
                                                                  solution[5],
                                                                  solution[6],
                                                                  performance['Precision'],
                                                                  performance['Recall'],
                                                                  performance['F1'],
                                                                  performance['WD'],
                                                                  performance['Pk'],
                                                                  new_fitness))

    return new_fitness


def fitness_func_60_comun(solution, solution_idx):
    global cont_file
    global tot
    global cont_generation
    global initial_flag
    global tiempo_estimado

    anterior_fitness = 0
    new_fitness_sum = 0

    # aqui hacemos la segmentacion y la evaluacion

    # introduccion del archivo

    for path_seg in lista_validacion:       #para cada uno de los archivos en la lista
        tiempo_estimado_inicial = time()
        # comprobamos si existe el archivo gt

        path_base = "VTT\\"
        split_path = path_seg.split('\\')                                                       # separamos en \ el path de entrada para conseguir el path de salida a partir de este
        num_path = split_path[-1]                                                               # obtenemos el numero.txt
        num_path = num_path.split('.')                                                          # separamos por el punto
        num_path = num_path[0]                                                                  # nos quedamos con el numero
        name_path = split_path[-2]                                                              # nos quedamos con el nombre de las noticias
        path_ev = path_base + "txt_gt\\60mins\\gt\\" + name_path + "\\" + num_path + ".txt"      # este es el path donde se encuentra el ground truth
        if not os.path.exists(path_ev):
            print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
            return 0

        # realizamos la segmentacion

        myNews = Segmentation_60(path_seg, "00:59:59", solution[0], (solution[1], solution[2]),
                                 (solution[3], solution[4], solution[5]),
                                 (solution[6],))                                                # creamos la segmentacion con los hiperparametros obtenidos en solution

        # evaluamos

        performance = make_evaluate(myNews, path_seg, "00:59:59", False)

        # pasamos los datos de evaluacion por el algoritmo de fitness

        new_fitness_solo = algoritmo_fitness(performance)
        new_fitness_sum = new_fitness_solo + anterior_fitness
        anterior_fitness = new_fitness_sum

        #guardamos los datos en un csv

        if cont_list_val == 0 and initial_flag == True:
            try:
                os.remove("hist_validation.csv")                                                            #intentamos eliminar el archivo la primera vez para evitar duplicados
            except:
                pass

        with open("hist_validation.csv", "a") as temporalEv:                                                # abrimos un archivo csv
            if cont_list_val == 0 and initial_flag == True:
                temporalEv.writelines('Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')                          # agregamos las cabeceras la primera vez
                initial_flag = False
            temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(path_seg.split('\\')[-2],
                                                                      path_seg.split('\\')[-1],                             # agregamos en cada vuelta los valores del rendimiento
                                                                      solution[0],
                                                                      solution[1],
                                                                      solution[2],
                                                                      solution[3],
                                                                      solution[4],
                                                                      solution[5],
                                                                      solution[6],
                                                                      performance['Precision'],
                                                                      performance['Recall'],
                                                                      performance['F1'],
                                                                      performance['WD'],
                                                                      performance['Pk'],
                                                                      new_fitness_solo))

        cont_file += 1
        count_vtt = len(lista_validacion)
        count_vtt = (count_vtt * tot) + (2*count_vtt)
        porc_gen = (cont_file / count_vtt) * 100
        print("{:.2f} %".format(porc_gen))

        tiempo_estimado_final = time()
        tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial  # segundos que tarda en evaluarse un archivo
        tiempo_estimado += tiempo_actual_archivo  # sumamos todos los datos de tiempos
        tiempo_estimado_medio = tiempo_estimado / cont_file  # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
        tiempo_estimado_out = tiempo_estimado_medio * (
                count_vtt - cont_file)  # tiempo estimado para finalizar en segundos
        print("\nTiempo estimado de finalizacion: {}\n".format(make_temp(0, tiempo_estimado_out, False)))

    return new_fitness_sum/len(lista_validacion)


def fitness_func_5_comun(solution, solution_idx):
    # aqui hacemos la segmentacion y la evaluacion
    global cont_file
    global tot
    global cont_generation
    global initial_flag
    global tiempo_estimado

    anterior_fitness = 0
    new_fitness_sum = 0
    #introduccion del archivo

    for path_seg in lista_validacion:       #para cada uno de los archivos en la lista
        #comprobamos si existe el archivo gt
        tiempo_estimado_inicial = time()

        path_base = "VTT\\"
        split_path = path_seg.split('\\')                                                               # separamos en \ el path de entrada para conseguir el path de salida a partir de este
        num_path = split_path[-1]                                                                       # obtenemos el numero.txt
        num_path = num_path.split('.')                                                                  # separamos por el punto
        num_path = num_path[0]                                                                          # nos quedamos con el numero
        name_path = split_path[-2]                                                                      # nos quedamos con el nombre de las noticias
        path_ev = path_base + "txt_gt\\5mins\\gt\\" + name_path + "\\" + num_path + ".txt"              # este es el path donde se encuentra el ground truth
        if not os.path.exists(path_ev):
            print("no existe el archivo Ground Truth, no se puede realizar la evaluacion")
            return 0

        #realizamos la segmentacion

        myNews = Segmentation_60(path_seg, "00:05:00", solution[0], (solution[1], solution[2]), (solution[3], solution[4], solution[5]), (solution[6],))         #creamos la segmentacion con los hiperparametros obtenidos en solution

        #evaluamos

        performance = make_evaluate(myNews, path_seg, "00:05:00", False)

        #pasamos los datos de evaluacion por el algoritmo de fitness

        new_fitness_solo = algoritmo_fitness(performance)
        new_fitness_sum = new_fitness_solo + anterior_fitness
        anterior_fitness = new_fitness_sum

        #guardamos los datos en un csv

        if cont_list_val == 0 and initial_flag == True:
            try:
                os.remove("hist_validation.csv")                                                            #intentamos eliminar el archivo la primera vez para evitar duplicados
            except:
                pass

        with open("hist_validation.csv", "a") as temporalEv:                                                # abrimos un archivo csv
            if cont_list_val == 0 and initial_flag == True:
                temporalEv.writelines('Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')                          # agregamos las cabeceras la primera vez
                initial_flag = False
            temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(path_seg.split('\\')[-2],
                                                                      path_seg.split('\\')[-1],                             # agregamos en cada vuelta los valores del rendimiento
                                                                      solution[0],
                                                                      solution[1],
                                                                      solution[2],
                                                                      solution[3],
                                                                      solution[4],
                                                                      solution[5],
                                                                      solution[6],
                                                                      performance['Precision'],
                                                                      performance['Recall'],
                                                                      performance['F1'],
                                                                      performance['WD'],
                                                                      performance['Pk'],
                                                                      new_fitness_solo))

        cont_file += 1
        count_vtt = len(lista_validacion)
        count_vtt = (count_vtt * tot) + (2*count_vtt)                               #restamos count_vtt para dejar espacio a la comprobacion final en los porcentajes
        porc_gen = (cont_file / count_vtt) * 100

        print("{:.2f} %".format(porc_gen))

        tiempo_estimado_final = time()
        tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial  # segundos que tarda en evaluarse un archivo
        tiempo_estimado += tiempo_actual_archivo  # sumamos todos los datos de tiempos
        tiempo_estimado_medio = tiempo_estimado / cont_file  # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
        tiempo_estimado_out = tiempo_estimado_medio * (
                count_vtt - cont_file)  # tiempo estimado para finalizar en segundos
        print("\nTiempo estimado de finalizacion: {}\n".format(make_temp(0, tiempo_estimado_out, False)))


    return new_fitness_sum/len(lista_validacion)


def algoritmo_fitness(performance):
    f1 = float(performance['F1'])
    wd = float(performance['WD'])

    new_fitness = 2 * ((f1 * (1 - wd))/(f1 + (1 - wd)))         #media armonica de f1 y wd
    return new_fitness


def on_generation(ga_instance):
    global cont_generation
    tot = ga_instance.num_generations
    cont_generation += 1
    count_vtt = len(lista_validacion)
    count_vtt = count_vtt * tot
    porc_gen = (cont_generation / count_vtt) * 100
    porc_gen += val_progress
    print("{:.2f} %" .format(porc_gen))


def on_start(ga_instance):
    global tot
    tot = ga_instance.num_generations * ga_instance.sol_per_pop


def make_validation_comun(time_limit):

    global cont_list_val
    global val_progress
    global cont_generation
    global tot
    global cont_file

    lista_datos_validacion = []
    make_global_list()
    count_vtt = len(lista_validacion)
    count_progress = 0
    tiempo_estimado = 0

    if time_limit == "00:59:59":
        count_progress += 1
        tiempo_inicial = time()

        ga_instance = pg.GA(num_generations=10,
                            sol_per_pop=6,
                            num_genes=7,
                            num_parents_mating=2,
                            initial_population=[[0.245, 0.23, 0.1, 0.256, 1, 0.15, 0.614],
                                                [0.345, 0.43, 0.3, 0.132, 1, 0.15, 0.670],
                                                [0.145, 0.56, 0.2, 0.101, 1, 0.32, 0.600],
                                                [0.270, 0.92, 0.1, 0.256, 1, 0.21, 0.520],
                                                [0.465, 0, 0.9, 0.342, 1, 0.56, 0.614],
                                                [0.122, 0.23, 0.1, 0.156, 1, 0.15, 0.650]],
                            gene_space=[{"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001},
                                        {"low": 0, "high": 1, "step": 0.0001}, [0, 1, 2, 3], {"low": 0, "high": 1, "step": 0.0001},
                                        {"low": 0, "high": 1, "step": 0.0001}],
                            fitness_func=fitness_func_60_comun,
                            mutation_type="random",
                            mutation_probability=0.4,
                            on_start=on_start
                            )

        ga_instance.run()
        x, y, z = ga_instance.best_solution()

        #probamos los HIPERPARAMS

        for val_file in lista_validacion:

            tiempo_estimado_inicial = time()

            myNews = Segmentation_60(val_file, "00:59:59", x[0], (x[1], x[2]), (x[3], x[4], x[5]), (x[6],))
            performance = make_evaluate(myNews, val_file, "00:59:59", False)

            # guardamos los datos en un csv

            if cont_list_val == 0:
                try:
                    os.remove("validation_60.csv")  # intentamos eliminar el archivo la primera vez para evitar duplicados
                except:
                    pass

            with open("validation_60.csv", "a") as temporalEv:  # abrimos un archivo csv
                if cont_list_val == 0:
                    temporalEv.writelines(
                        'Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')  # agregamos las cabeceras la primera vez
                temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(val_file.split('\\')[-2],
                                                                                              val_file.split('\\')[-1],
                                                                                              x[0],
                                                                                              x[1],
                                                                                              x[2],
                                                                                              x[3],
                                                                                              x[4],
                                                                                              x[5],
                                                                                              x[6],
                                                                                              performance['Precision'],
                                                                                              performance['Recall'],
                                                                                              performance['F1'],
                                                                                              performance['WD'],
                                                                                              performance['Pk'],
                                                                                              algoritmo_fitness(performance)))



            cont_file += 1
            count_vtt = len(lista_validacion)
            count_vtt = (count_vtt * tot) + (2*count_vtt)                               #restamos count_vtt para dejar espacio a la comprobacion final en los porcentajes
            porc_gen = (cont_file / count_vtt) * 100
            print("{:.2f} %".format(porc_gen))

            tiempo_estimado_final = time()
            tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial  # segundos que tarda en evaluarse un archivo
            tiempo_estimado += tiempo_actual_archivo  # sumamos todos los datos de tiempos
            tiempo_estimado_medio = tiempo_estimado / cont_file  # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
            tiempo_estimado_out = tiempo_estimado_medio * (
                    count_vtt - cont_file)  # tiempo estimado para finalizar en segundos
            print("\nTiempo estimado de finalizacion: {}\n".format(make_temp(0, tiempo_estimado_out, False)))

        print("\n||||||||| HIPERPARAMETROS SOLUCION ||||||||||")
        print("\nPara el archivo {}\n" .format(lista_validacion[cont_list_val]))
        hiperparameters_table = [['Betta (TDM Decorrelator)', x[0]],
                                 ['varianza (GPA preSDM Gaussian)', x[1]],
                                 ['w (GPA preSDM Gaussian Weight)', x[2]],
                                 ['PBMM-th (SDM PBMM threshold)', x[3]],
                                 ['OIM (SDM fail oportunities)', x[4]],
                                 ['CB-th (SDM checkback threshold)', x[5]],
                                 ['FBBCM-th (LCM FBBCM-threshold)', x[6]]]
        print(tabulate(hiperparameters_table, tablefmt="grid"))
        print("\nver resultados en el archivo validation_60.csv en el archivo raiz del programa\n")

        tiempo_final = time()

        make_temp(tiempo_inicial, tiempo_final, show=True)

    elif time_limit == "00:05:00":
        count_progress += 1
        tiempo_inicial = time()

        ga_instance = pg.GA(num_generations=10,
                            sol_per_pop=6,
                            num_genes=7,
                            num_parents_mating=2,
                            initial_population=[[0.245, 0.23, 0.1, 0.256, 1, 0.15, 0.614],
                                                [0.465, 0, 0.9, 0.342, 1, 0.56, 0.614],
                                                [0.345, 0.43, 0.3, 0.132, 1, 0.15, 0.670],
                                                [0.145, 0.56, 0.2, 0.101, 1, 0.32, 0.600],
                                                [0.270, 0.92, 0.1, 0.256, 1, 0.21, 0.520],
                                                [0.122, 0.23, 0.1, 0.156, 1, 0.15, 0.650]],
                            gene_space=[{"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001},
                                        {"low": 0, "high": 1, "step": 0.0001}, [0, 1, 2, 3], {"low": 0, "high": 1, "step": 0.0001},
                                        {"low": 0, "high": 1, "step": 0.0001}],
                            fitness_func=fitness_func_5_comun,
                            mutation_type="random",
                            mutation_probability=0.4,
                            on_start=on_start
                            )

        ga_instance.run()
        x, y, z = ga_instance.best_solution()

        # probamos los HIPERPARAMS

        for val_file in lista_validacion:

            tiempo_estimado_inicial = time()
            myNews = Segmentation_60(val_file, "00:05:00", x[0], (x[1], x[2]),
                                     (x[3], x[4], x[5]), (x[6],))
            performance = make_evaluate(myNews, val_file, "00:05:00", False)

            # guardamos los datos en un csv

            if cont_list_val == 0:
                try:
                    os.remove("validation_5.csv")  # intentamos eliminar el archivo la primera vez para evitar duplicados
                except:
                    pass

            with open("validation_5.csv", "a") as temporalEv:  # abrimos un archivo csv
                if cont_list_val == 0:
                    temporalEv.writelines(
                        'Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')  # agregamos las cabeceras la primera vez
                temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(val_file.split('\\')[-2],
                                                                                              val_file.split('\\')[-1],
                                                                                              x[0],
                                                                                              x[1],
                                                                                              x[2],
                                                                                              x[3],
                                                                                              x[4],
                                                                                              x[5],
                                                                                              x[6],
                                                                                              performance['Precision'],
                                                                                              performance['Recall'],
                                                                                              performance['F1'],
                                                                                              performance['WD'],
                                                                                              performance['Pk'],
                                                                                              algoritmo_fitness(performance)))

            cont_file += 1
            count_vtt = len(lista_validacion)
            count_vtt = (count_vtt * tot) + (2*count_vtt)  # sumamos count_vtt para dejar espacio a la comprobacion final en los porcentajes
            porc_gen = (cont_file / count_vtt) * 100
            print("{:.2f} %".format(porc_gen))

            tiempo_estimado_final = time()
            tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial  # segundos que tarda en evaluarse un archivo
            tiempo_estimado += tiempo_actual_archivo  # sumamos todos los datos de tiempos
            tiempo_estimado_medio = tiempo_estimado / cont_file  # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
            tiempo_estimado_out = tiempo_estimado_medio * (
                    count_vtt - cont_file)  # tiempo estimado para finalizar en segundos
            print("\nTiempo estimado de finalizacion: {}\n".format(make_temp(0, tiempo_estimado_out, False)))

        print("\n||||||||| HIPERPARAMETROS SOLUCION ||||||||||")
        print("\nPara el archivo {}\n".format(lista_validacion[cont_list_val]))
        hiperparameters_table = [['Betta (TDM Decorrelator)', x[0]],
                                 ['varianza (GPA preSDM Gaussian)', x[1]],
                                 ['w (GPA preSDM Gaussian Weight)', x[2]],
                                 ['PBMM-th (SDM PBMM threshold)', x[3]],
                                 ['OIM (SDM fail oportunities)', x[4]],
                                 ['CB-th (SDM checkback threshold)', x[5]],
                                 ['FBBCM-th (LCM FBBCM-threshold)', x[6]]]
        print(tabulate(hiperparameters_table, tablefmt="grid"))
        print("\nver resultados en el archivo validation_60.csv en el archivo raiz del programa\n")

        tiempo_final = time()

        make_temp(tiempo_inicial, tiempo_final, show=True)

    cont_generation = 0  # ojo estaba a -1
    tot = 0
    cont_file = 0


def make_validation_propio(time_limit, flag_first_time, data_stage1):

    global cont_list_val
    global val_progress
    global cont_generation

    lista_datos_validacion = []
    make_global_list()
    count_vtt = len(lista_validacion)
    count_progress = 0
    tiempo_estimado = 0

    if time_limit == "00:59:59":
        for val_file in lista_validacion:
            count_progress += 1
            print("\nrealizando validacion con el archivo {}" .format(val_file))

            if flag_first_time:

                ga_instance = pg.GA(num_generations=2,
                                    sol_per_pop=7,
                                    num_genes=7,
                                    num_parents_mating=2,
                                    initial_population=[[random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()],
                                                        [random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()],
                                                        [random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()],
                                                        [random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()],
                                                        [random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()],
                                                        [random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()],
                                                        [random.random(), random.random(), random.random(), random.random(), random.randint(0, 5), random.random(), random.random()]],
                                    gene_space=[{"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001},
                                                {"low": 0, "high": 1, "step": 0.0001}, [0, 1, 2, 3], {"low": 0, "high": 1, "step": 0.0001},
                                                {"low": 0, "high": 1, "step": 0.0001}],
                                    fitness_func=fitness_func_60_propio,
                                    mutation_type="random",
                                    mutation_probability=0.15,
                                    )
            else:

                ga_instance = pg.GA(num_generations=2,
                                    sol_per_pop=7,
                                    num_genes=7,
                                    num_parents_mating=2,
                                    initial_population=[[data_stage1[0][0][0], data_stage1[0][0][1], data_stage1[0][0][2], data_stage1[0][0][3], data_stage1[0][0][4], data_stage1[0][0][5], data_stage1[0][0][6]],
                                                        [data_stage1[1][0][0], data_stage1[1][0][1], data_stage1[1][0][2], data_stage1[1][0][3], data_stage1[1][0][4], data_stage1[1][0][5], data_stage1[1][0][6]],
                                                        [data_stage1[2][0][0], data_stage1[2][0][1], data_stage1[2][0][2], data_stage1[2][0][3], data_stage1[2][0][4], data_stage1[2][0][5], data_stage1[2][0][6]],
                                                        [data_stage1[3][0][0], data_stage1[3][0][1], data_stage1[3][0][2], data_stage1[3][0][3], data_stage1[3][0][4], data_stage1[3][0][5], data_stage1[3][0][6]],
                                                        [data_stage1[4][0][0], data_stage1[4][0][1], data_stage1[4][0][2], data_stage1[4][0][3], data_stage1[4][0][4], data_stage1[4][0][5], data_stage1[4][0][6]],
                                                        [data_stage1[5][0][0], data_stage1[5][0][1], data_stage1[5][0][2], data_stage1[5][0][3], data_stage1[5][0][4], data_stage1[5][0][5], data_stage1[5][0][6]],
                                                        [data_stage1[6][0][0], data_stage1[6][0][1], data_stage1[6][0][2], data_stage1[6][0][3], data_stage1[6][0][4], data_stage1[6][0][5], data_stage1[6][0][6]]],
                                    gene_space=[{"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001},
                                                {"low": 0, "high": 1, "step": 0.0001}, [0, 1, 2, 3], {"low": 0, "high": 1, "step": 0.0001},
                                                {"low": 0, "high": 1, "step": 0.0001}],
                                    fitness_func=fitness_func_60_propio,
                                    mutation_type="random",
                                    mutation_probability=0.15,
                                    )

            ga_instance.run()
            x, y, z = ga_instance.best_solution()

            #probamos los HIPERPARAMS

            myNews = Segmentation_60(val_file, "00:59:59", x[0], (x[1], x[2]),
                                     (x[3], x[4], x[5]), (x[6],))
            performance = make_evaluate(myNews, val_file, "00:59:59", False)            #this is the fitness solution I will show in a graphic

            # guardamos los datos en un csv

            if cont_list_val == 0:
                try:
                    os.remove("validation_60.csv")  # intentamos eliminar el archivo la primera vez para evitar duplicados
                except:
                    pass

            with open("validation_60.csv", "a") as temporalEv:  # abrimos un archivo csv
                if cont_list_val == 0:
                    temporalEv.writelines(
                        'Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')  # agregamos las cabeceras la primera vez
                temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(val_file.split('\\')[-2],
                                                                                              val_file.split('\\')[-1],
                                                                                              x[0],
                                                                                              x[1],
                                                                                              x[2],
                                                                                              x[3],
                                                                                              x[4],
                                                                                              x[5],
                                                                                              x[6],
                                                                                              performance['Precision'],
                                                                                              performance['Recall'],
                                                                                              performance['F1'],
                                                                                              performance['WD'],
                                                                                              performance['Pk'],
                                                                                              y))

            lista_datos_validacion.append([x, y])
            cont_list_val += 1
        cont_list_val = 0
        return lista_datos_validacion

    elif time_limit == "00:05:00":
        for val_file in lista_validacion:
            count_progress += 1
            tiempo_estimado_inicial = time()
            print("realizando validacion con el archivo {}".format(val_file))

            ga_instance = pg.GA(num_generations=10,
                                sol_per_pop=6,
                                num_genes=7,
                                num_parents_mating=2,
                                initial_population=[[0.245, 0.23, 0.1, 0.256, 1, 0.15, 0.614],
                                                    [0.345, 0.43, 0.3, 0.132, 1, 0.15, 0.670],
                                                    [0.145, 0.56, 0.2, 0.101, 1, 0.32, 0.600],
                                                    [0.270, 0.92, 0.1, 0.256, 1, 0.21, 0.520],
                                                    [0.245, 0.11, 0.2, 0.276, 1, 0.19, 0.500],
                                                    [0.245, 0.43, 0.3, 0.268, 1, 0.15, 0.780],
                                                    [0.210, 0.23, 0.7, 0.467, 1, 0.15, 0.210],
                                                    [0.421, 0.21, 0.9, 0.678, 1, 0.12, 0.614],
                                                    [0.465, 0, 0.9, 0.342, 1, 0.56, 0.614],
                                                    [0.122, 0.23, 0.1, 0.156, 1, 0.15, 0.650]],
                                gene_space=[{"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001}, {"low": 0, "high": 1, "step": 0.0001},
                                            {"low": 0, "high": 1, "step": 0.0001}, [0, 1, 2, 3], {"low": 0, "high": 1, "step": 0.0001},
                                            {"low": 0, "high": 1, "step": 0.0001}],
                                fitness_func=fitness_func_5_propio,
                                mutation_type="random",
                                mutation_probability=0.4,
                                on_generation=on_generation,
                                )

            ga_instance.run()
            x, y, z = ga_instance.best_solution()

            # probamos los HIPERPARAMS

            myNews = Segmentation_60(val_file, "00:05:00", x[0], (x[1], x[2]),
                                     (x[3], x[4], x[5]), (x[6],))
            performance = make_evaluate(myNews, val_file, "00:05:00", False)

            # guardamos los datos en un csv

            if cont_list_val == 0:
                try:
                    os.remove("validation_5.csv")  # intentamos eliminar el archivo la primera vez para evitar duplicados
                except:
                    pass

            with open("validation_5.csv", "a") as temporalEv:  # abrimos un archivo csv
                if cont_list_val == 0:
                    temporalEv.writelines(
                        'Noticia_principal,Numero_TD,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Precision,Recall,F1,WD,Pk,Rendimiento\n')  # agregamos las cabeceras la primera vez
                temporalEv.writelines("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(val_file.split('\\')[-2],
                                                                                              val_file.split('\\')[-1],
                                                                                              x[0],
                                                                                              x[1],
                                                                                              x[2],
                                                                                              x[3],
                                                                                              x[4],
                                                                                              x[5],
                                                                                              x[6],
                                                                                              performance['Precision'],
                                                                                              performance['Recall'],
                                                                                              performance['F1'],
                                                                                              performance['WD'],
                                                                                              performance['Pk'],
                                                                                              y))

            print("\n||||||||| HIPERPARAMETROS SOLUCION ||||||||||")
            print("\nPara el archivo {}\n".format(lista_validacion[cont_list_val]))
            hiperparameters_table = [['Betta (TDM Decorrelator)', x[0]],
                                     ['varianza (GPA preSDM Gaussian)', x[1]],
                                     ['w (GPA preSDM Gaussian Weight)', x[2]],
                                     ['PBMM-th (SDM PBMM threshold)', x[3]],
                                     ['OIM (SDM fail oportunities)', x[4]],
                                     ['CB-th (SDM checkback threshold)', x[5]],
                                     ['FBBCM-th (LCM FBBCM-threshold)', x[6]]]
            print(tabulate(hiperparameters_table, tablefmt="grid"))
            print("\n||||||||| RENDIMIENTO ||||||||||\n")
            performance_table = [['Precision', performance['Precision']],
                                     ['Recall', performance['Recall']],
                                     ['F1', performance['F1']],
                                     ['WD', performance['WD']],
                                     ['Pk', performance['Pk']],
                                     ['Fitness', y]]
            print(tabulate(performance_table, tablefmt="grid"))

            lista_datos_validacion.append([x, y])

            tiempo_estimado_final = time()
            tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial  # segundos que tarda en evaluarse un archivo
            tiempo_estimado += tiempo_actual_archivo  # sumamos todos los datos de tiempos
            tiempo_estimado_medio = tiempo_estimado / count_progress  # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
            tiempo_estimado_out = tiempo_estimado_medio * (
                        count_vtt - count_progress)  # tiempo estimado para finalizar en segundos
            print("\nTiempo estimado de finalizacion: {}\n".format(make_temp(0, tiempo_estimado_out, False)))
            percent_progress = (count_progress / count_vtt) * 100
            val_progress = percent_progress
            cont_generation = 0
            print("\n{:.2f} % completado\n".format(percent_progress))

            cont_list_val += 1
        cont_list_val = 0
        return lista_datos_validacion


def make_global_list():

    global lista_validacion

    lista_validacion = []
    carpeta_validacion = "VTT\\txt_gt\\60mins\\txt\\Diana"
    while not os.path.exists(carpeta_validacion):                                            # esperamos a una entrada de una carpeta que exista
        print("No existe la direccion suministrada")

    for file_text in os.listdir(carpeta_validacion):                                        # recorremos los archivos que hay en dicha carpeta
        if os.path.isdir(carpeta_validacion + "\\" + file_text):                            # si es un directorio
            for file_text_in in os.listdir(carpeta_validacion + "\\" + file_text):          # recorremos otra vez los archivos de dicha carpeta
                lista_validacion.append(carpeta_validacion + "\\" + file_text + "\\" + file_text_in)
        else:
            lista_validacion.append(carpeta_validacion + "\\" + file_text)


def make_verification_model(sol_th, cut_sol, time_limit):

    death_list = []
    eval_texts = ""
    comprobante = ""
    fitness_total = 0
    fitness_norm = []
    sp_betta = 0
    sp_var = 0
    sp_w = 0
    sp_pbmm_th = 0
    sp_oim = 0
    sp_cb_th = 0
    sp_fbbcm_th = 0
    txts_list = []
    tiempo_estimado = 0
    count_progress = 0
    media_f1 = []
    media_WD = []
    media_sols = []
    lista_betta = []
    lista_var = []
    lista_w = []
    lista_pbmm_th = []
    lista_oim = []
    lista_cb_th = []
    lista_fbbcm_th = []

    data_eval = pd.DataFrame(columns=['solucion', 'Noticia_principal', 'Numero_TD', 'BETTA(param)', 'VAR(param)',
                                      'W(param)', 'PBMM_th(param)', 'OIM(param)', 'CB_th(param)', 'FBBCM_th(param)',
                                      'Precision', 'Recall', 'F1', 'WD', 'Pk'])
    data_out = data_eval.drop(['Noticia_principal', 'Numero_TD'], axis=1)

    #buscamos el archivo validation_5.csv necesario para la post evaluacion
    if time_limit == "00:05:00":
        if not os.path.exists("validation_5.csv"):
            print("no existe el archivo validation.csv con los resultados de validacion, por favor, realiza la validacion o "
                "guarda un archivo de validacion anterior en la carpeta raiz del programa\n")
            return -1

        #abrimos el csv con los datos de la validacion

        try:
            val_file = pd.read_csv("validation_5.csv")
        except:
            print("ha habido un problema al abrir el archivo validation.csv, volviendo al menu principal. \n")
            return -1

    #buscamos el archivo validation_60.csv necesario para la post evaluacion
    elif time_limit == "00:59:59":
        if not os.path.exists("validation_60.csv"):
            print("no existe el archivo validation.csv con los resultados de validacion, por favor, realiza la validacion o "
                "guarda un archivo de validacion anterior en la carpeta raiz del programa\n")
            return -1

        #abrimos el csv con los datos de la validacion

        try:
            val_file = pd.read_csv("validation_60.csv")
        except:
            print("ha habido un problema al abrir el archivo validation.csv, volviendo al menu principal. \n")
            return -1

    else:
        print("el tiempo establecido para el archivo de texto no son ni 5 ni 60 minutos, abortando\n")
        return -1

    #pedimos la direccion donde se van a encontrar el archivo (o los archivos/carpetas) sobre los que se va a realizar
    #la evaluacion

    while (not os.path.exists(eval_texts)) or (comprobante != "vtt" and comprobante != "txt" and (not os.path.isdir(eval_texts))):
        eval_texts = "VTT\\txt_gt\\60mins\\txt\\Diana_test"
        try:
            eval_texts_split = eval_texts.split(".")
            comprobante = eval_texts_split[-1]
        except:
            if os.path.isdir(eval_texts):
                pass
            else:
                print("Ha ocurrido un error al buscar la extension del archivo")

    #recorremos la lista de validacion eliminando los datos que se encuentran por debajo del threshold de soluciones

    num_sols = val_file.shape[0]

    if cut_sol:

        for i in range(num_sols):
            if val_file['Rendimiento'][i] < sol_th:
                death_list.append(i)

        val_file.drop(death_list, axis=0, inplace=True)
        val_file.reset_index(inplace=True, drop=True)
        num_sols = val_file.shape[0]

    #ahora añadimos al grupo de soluciones la solucion derivada de la suma ponderada de los pesos de las buenas soluciones

    for i in range(num_sols):
        fitness_total += val_file['Rendimiento'][i]         #suma de todos los rendimientos

    for i in range(num_sols):
        fitness_norm.append(float(val_file['Rendimiento'][i]/fitness_total))    #almacenamos la ponderacion de cada caso
        if fitness_norm[i] > 1 or fitness_norm[i] < 0:
            print("se ha producido un error calculando la normalizacion de los parametros\n")
            return -1

    if sum(fitness_norm) < 0.98 or sum(fitness_norm) > 1.02:
        print("ha ocurrido un error calculando la normalizacion de los parametros (la suma de la normalizacion no se "
              "establece en 1")

    #realizamos la suma ponderada (ya tenemos todos los datos) de cada uno de los parametros

    for i in range(num_sols):
        sp_betta += fitness_norm[i] * val_file['BETTA(param)'][i]
        sp_var += fitness_norm[i] * val_file['VAR(param)'][i]
        sp_w += fitness_norm[i] * val_file['W(param)'][i]
        sp_pbmm_th += fitness_norm[i] * val_file['PBMM_th(param)'][i]
        sp_oim += fitness_norm[i] * val_file['OIM(param)'][i]
        sp_cb_th += fitness_norm[i] * val_file['CB_th(param)'][i]
        sp_fbbcm_th += fitness_norm[i] * val_file['FBBCM_th(param)'][i]

    sp_oim = round(sp_oim)                          #redondeamos oim ya que queremos un numero entero

    #añadimos la solucion custom a nuestro dataframe

    df_aux = pd.DataFrame(
        {val_file.columns[0]: "custom_params", val_file.columns[1]: "custom_params", val_file.columns[2]: sp_betta,
         val_file.columns[3]: sp_var, val_file.columns[4]: sp_w, val_file.columns[5]: sp_pbmm_th,
         val_file.columns[6]: sp_oim, val_file.columns[7]: sp_cb_th, val_file.columns[8]: sp_fbbcm_th}, index=[0])

    val_file = pd.merge(val_file, df_aux, how="outer")
    val_file.drop([val_file.columns[0], val_file.columns[1], val_file.columns[9], val_file.columns[10], val_file.columns[11],
                   val_file.columns[12], val_file.columns[13], val_file.columns[14]], axis=1, inplace=True)

    num_sols = val_file.shape[0]

    #aqui ya tenemos la lista de parametros que queremos evaluar, por lo tanto, evaluamos

    #buscamos los txt donde vamos a evaluar

    if os.path.isdir(eval_texts):
        for primer_nivel in os.listdir(eval_texts):
            new_path = eval_texts + "\\" + primer_nivel
            if os.path.isdir(new_path):
                for segundo_nivel in os.listdir(new_path):
                    new_second_path = new_path + "\\" + segundo_nivel
                    if os.path.isdir(new_second_path):
                        print("error, sistema de archivos demasiado profundo, maximo 2 carpetas de profundidad\n")
                        return -1
                    else:
                        txts_list.append(new_second_path)
            else:
                txts_list.append(new_path)
    else:
        txts_list.append(eval_texts)

    #lista de evaluacion almacenada en txts_list

    count_vtt = num_sols * len(txts_list)

    for i in range(num_sols):                               #recorremos el indice de cada una de las soluciones
        for text_file in txts_list:                         #recorremos cada archivo a evaluar
            tiempo_estimado_inicial = time()


           #segmentacion

            myNews = Segmentation_60(text_file, time_limit, val_file['BETTA(param)'][i],
                                     (val_file['VAR(param)'][i], val_file['W(param)'][i]),
                                     (val_file['PBMM_th(param)'][i], val_file['OIM(param)'][i], val_file['CB_th(param)'][i]),
                                     (val_file['FBBCM_th(param)'][i],))

            #evaluacion
            muestra_hiperparametros(myNews)
            performance = make_evaluate(myNews, text_file, time_limit, True)

            #almacenamos en un dataframe para poder tratar los datos mas tarde

            data_aux = pd.DataFrame(
                {data_eval.columns[0]: i+1, data_eval.columns[1]: text_file.split("\\")[-2],
                 data_eval.columns[2]: text_file.split("\\")[-1],
                 data_eval.columns[3]: val_file['BETTA(param)'][i], data_eval.columns[4]: val_file['VAR(param)'][i],
                 data_eval.columns[5]: val_file['W(param)'][i], data_eval.columns[6]: val_file['PBMM_th(param)'][i],
                 data_eval.columns[7]: val_file['OIM(param)'][i], data_eval.columns[8]: val_file['CB_th(param)'][i],
                 data_eval.columns[9]: val_file['FBBCM_th(param)'][i], data_eval.columns[10]: performance['Precision'],
                 data_eval.columns[11]: performance['Recall'], data_eval.columns[12]: performance['F1'],
                 data_eval.columns[13]: performance['WD'], data_eval.columns[14]: performance['Pk']},
                index=[0])

            data_eval = pd.merge(data_eval, data_aux, how="outer")

            #en data_eval se encuentran todos los datos

            #realizamos la media de las evaluaciones PARA UNA MISMA SOLUCION

            #tiempo y porcentaje

            count_progress += 1
            tiempo_estimado_final = time()
            tiempo_actual_archivo = tiempo_estimado_final - tiempo_estimado_inicial  # segundos que tarda en evaluarse un archivo
            tiempo_estimado += tiempo_actual_archivo  # sumamos todos los datos de tiempos
            tiempo_estimado_medio = tiempo_estimado / count_progress  # dividimos entre los que llevamos consiguiendo la media de tiempo que tarda
            tiempo_estimado_out = tiempo_estimado_medio * (count_vtt - count_progress)  # tiempo estimado para finalizar en segundos
            print("\nTiempo estimado de finalizacion: {}\n".format(make_temp(0, tiempo_estimado_out, False)))
            percent_progress = (count_progress / count_vtt) * 100
            print("\n{:.2f} % completado\n".format(percent_progress))

    for i in range(num_sols):
        filtro_solucion = data_eval['solucion'] == i+1
        solucion_actual = data_eval[filtro_solucion].reset_index(drop=True)

        #lista_precision = []
        #lista_recall = []
        lista_f1 = []
        lista_WD = []
        #lista_Pk = []


        for j in range(solucion_actual.shape[0]):
            #lista_precision.append(solucion_actual['Precision'][j])
            #lista_recall.append(solucion_actual['Recall'][j])
            lista_f1.append(solucion_actual['F1'][j])
            lista_WD.append(solucion_actual['WD'][j])
            #lista_Pk.append(solucion_actual['Pk'][j])

        #media_precision.append(sum(lista_precision)/len(lista_precision))
        #media_recall.append(sum(lista_recall) / len(lista_recall))
        media_f1.append(sum(lista_f1) / len(lista_f1))
        media_WD.append(sum(lista_WD) / len(lista_WD))
        #media_Pk.append(sum(lista_Pk) / len(lista_Pk))

        lista_betta.append(solucion_actual['BETTA(param)'][0])
        lista_var.append(solucion_actual['VAR(param)'][0])
        lista_w.append(solucion_actual['W(param)'][0])
        lista_pbmm_th.append(solucion_actual['PBMM_th(param)'][0])
        lista_oim.append(solucion_actual['OIM(param)'][0])
        lista_cb_th.append(solucion_actual['CB_th(param)'][0])
        lista_fbbcm_th.append(solucion_actual['FBBCM_th(param)'][0])

    #en este punto tenemos la media de cada uno de los rendimientos. Para poder medirlos teniendo todos en consideracion
    #vamos a hacer una media de todos ellos

    for i in range(num_sols):
        media_sols.append((media_f1[i] * (1 - media_WD[i]))/(media_f1[i] + (1 - media_WD[i])))  #calculo del rendimiento general sobre un F1 (igual que la funcion de fitness)

    print("\n RENDIMIENTO POR SOLUCION \n")
    for i in range(num_sols):
        print("solucion {}: {} %" .format(i+1, media_sols[i]))

    #ya tenemos los rendimientos generales con los que podemos medir
    #cogemos el maximo
    #finalmente imprimimos por pantalla los parametros encontrados

    tmp = max(media_sols)
    index_max = media_sols.index(tmp)

    #almacenamos los parametros del maximo rendimiento general

    final_betta = lista_betta[index_max]
    final_var = lista_var[index_max]
    final_w = lista_w[index_max]
    final_pbmm_th = lista_pbmm_th[index_max]
    final_oim = lista_oim[index_max]
    final_CB_th = lista_cb_th[index_max]
    final_fbbcm_th = lista_fbbcm_th[index_max]

    print("\n||||||||| HIPERPARAMETROS SOLUCION FINAL ||||||||||")
    hiperparameters_table = [['Betta (TDM Decorrelator)', final_betta],
                             ['varianza (GPA preSDM Gaussian)', final_var],
                             ['w (GPA preSDM Gaussian Weight)', final_w],
                             ['PBMM-th (SDM PBMM threshold)', final_pbmm_th],
                             ['OIM (SDM fail oportunities)', final_oim],
                             ['CB-th (SDM checkback threshold)', final_CB_th],
                             ['FBBCM-th (LCM FBBCM-threshold)', final_fbbcm_th],
                             ['FITNESS', tmp]]
    print(tabulate(hiperparameters_table, tablefmt="grid"))

    return {
        "betta": final_betta,
        "var": final_var,
        "w": final_w,
        "pbmm_th": final_pbmm_th,
        "oim": final_oim,
        "CB_th": final_CB_th,
        "fbbcm_th": final_fbbcm_th,
        "fitness": tmp
    }
    #at this point we have the max fitness value in tmp and the parameters in the final_XXX variables


def salir():
    print('Saliendo')


def create_csv_AG(data_stage2, flag_first_time, ID_tracking):
    if flag_first_time == 1:
        try:
            os.remove("tracking_params.csv")  # intentamos eliminar el archivo la primera vez para evitar duplicados
        except:
            pass

    with open("tracking_params.csv", "a") as temporalEv:  # abrimos un archivo csv
        if flag_first_time == 1:
            temporalEv.writelines(
                'ID,BETTA(param),VAR(param),W(param),PBMM_th(param),OIM(param),CB_th(param),FBBCM_th(param),Rendimiento\n')  # agregamos las cabeceras la primera vez
        temporalEv.writelines("{},{},{},{},{},{},{},{},{}\n".format(ID_tracking,
                                                                  data_stage2["betta"],
                                                                  data_stage2["var"],
                                                                  data_stage2["w"],
                                                                  data_stage2["pbmm_th"],
                                                                  data_stage2["oim"],
                                                                  data_stage2["CB_th"],
                                                                  data_stage2["fbbcm_th"],
                                                                  data_stage2["fitness"]))
