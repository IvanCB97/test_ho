
"""archivo que contiene las funciones de ejecucion del menu principal"""

from method import *
import os


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Crear base de datos en formato txt', menu_tiempos_bbdd),
        '2': ('Realizar el recorrido completo de segmentacion', menu_tiempos_segmentacion),
        '3': ('Realizar la evaluacion del rendimiento individual', menu_custom_param_onebd),
        '4': ('Realizar la evaluacion del rendimiento completo', menu_custom_param_allbd),
        '5': ('Validacion / optimizacion de hiperaparmetros del modelo', menu_modelo),
        '6': ('PostValidacion, ajuste y comprobacion de los hiperparametros obtenidos', menu_custom_ajuste),
        '7': ('Salir', salir)
    }
    generar_menu(opciones, '7')


def menu_modelo():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Modelo comun (se tienen en cuenta todos los archivos por cada generacion)', menu_tiempos_modelo_comun),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Modelo propio (se entrena cada uno de los archivos de forma individual)', menu_tiempos_modelo_propio),                #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_custom_ajuste():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Modo restrictivo (se añade el modulo umbral limite) ', menu_tiempos_ajuste_restrictivo),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Modo permisivo ', menu_tiempos_ajuste_permisivo),                                                      #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_custom_param_onebd():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Parametros por defecto ', menu_tiempos_evaluacion_onebd),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Parametros personalizados ', menu_tiempos_evaluacion_onebd_p),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_custom_param_allbd():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Parametros por defecto ', menu_tiempos_evaluacion_allbd),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Parametros personalizados ', menu_tiempos_evaluacion_allbd_p),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_ajuste_restrictivo():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_verificacion_model_restric_5),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_verificacion_model_restric_60),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_ajuste_permisivo():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_verificacion_model_permis_5),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_verificacion_model_permis_60),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_modelo_comun():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_validation_5_comun),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_validation_60_comun),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_modelo_propio():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_validation_5_propio),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_validation_60_propio),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_evaluacion_allbd():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_segmentation_5_ev_allbd),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_segmentation_60_ev_allbd),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_evaluacion_allbd_p():
    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_segmentation_5_ev_allbd_p),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_segmentation_60_ev_allbd_p),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_evaluacion_onebd():

    if os.name == "nt":                                                              # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_segmentation_5_ev_onebd),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_segmentation_60_ev_onebd),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_evaluacion_onebd_p():

    if os.name == "nt":                                                              # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_segmentation_5_ev_onebd_p),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_segmentation_60_ev_onebd_p),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_segmentacion():

    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_segmentation_5),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_segmentation_60),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')


def menu_tiempos_bbdd():

    if os.name == "nt":  # borrado de pantalla segun OS
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    opciones = {
        '1': ('Para 5 minutos: 05:00 ', make_txt_5),               #eleccion para ejecutar todo en 5 minutos
        '2': ('Para 60 minutos: 59:59 ', make_txt_60),             #eleccion para ejecutar todo en 60 minutos
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')