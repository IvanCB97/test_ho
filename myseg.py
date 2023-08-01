"""Archivo que contiene la clase de segmentacion sobreescrita dedicada a los 60 minutos de telediario"""


import newsegmentation as ns

class Segmentation_60(ns.NewsSegmentation):
    """Clase sobreescrita que hereda de NewsSegmentation, esta clase esta diseñada especificamente para la
    segmentacion de noticias con duracion 60 minutos"""

    @staticmethod
    def _spatial_manager(r, param):
        """bloque de procesamiento del SDM
        inputs: r-> matriz R1 pasada por el GPA
                param-> param[0] = threshold PBMM
                        param[1] = OIM PBMM
                        param[2] = checkback threshold PBMM """

        x = ns.default_sdm(r, param)
        return x

    @staticmethod
    def _specific_language_model(s):
        """bloque de obtiencion directa de los embeddings (SLM)
        inputs: s-> lista de frases
        outputs: x-> lista de embeddings (tantos embeddings como frases)"""
        x = ns.default_slm(s)                                                   #s es una lista de frases que queremos comprobar entre sí
                                                                                #x es un vector de tantos valores como frases, eso se debe a que devuelve un vector numerico por cada frase
                                                                                #por lo tanto convierte una frase o conjunto de frases en un valor numerico segun su significado semantico
        return x

    @staticmethod
    def _later_correlation_manager(lm, s, t, param):
        """bloque de llamada directa al LCM
        inputs: lm-> objeto de la funcion de slm
                s-> lista de frases
                t-> lista de tiempos
                param-> threshold FBBCM
        outputs:
                _r-> matriz R2 final
                _s-> bloque de frase
                _t-> bloque de tiempos
        """
        _r, _s, _t = ns.default_lcm(lm, s, t, param)
        return _r, _s, _t

    @staticmethod
    def _database_transformation(path, op, time_limit):
        """Esta funcion realiza la parte inicial del proceso, convierte los vtt en txt"""
        return ns.default_dbt(path, op, time_limit)
