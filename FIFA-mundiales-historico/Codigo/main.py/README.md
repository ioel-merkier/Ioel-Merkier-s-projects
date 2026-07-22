from funciones import *
import csv

archivo_1 = "partidos.csv"
archivo_2 = "ranking_fifa.csv"

def promedio_asistentes(archivo_1, archivo_2):
    lista_reducida = extraer_ordenar(archivo_1)
    if lista_reducida == None:
        return
    
    reporte = ""
    i=0
    while i<len(lista_reducida):
        cantidad_asistentes = 0
        cant_partidos = 0
        
    
        while i < len(lista_reducida) - 1 and lista_reducida[i][0]==lista_reducida[i+1][0]:
            cantidad_asistentes+=lista_reducida[i][1]
            cant_partidos += 1
            i+=1
            
        cantidad_asistentes += lista_reducida[i][1]
        cant_partidos += 1
        
        if cant_partidos != 0:
            promedio_asistentes = cantidad_asistentes / cant_partidos
            year = lista_reducida[i-1][0]
            reporte += f"Promedio de asistentes en el mundial {year}: {round(promedio_asistentes)}\n"

        i+=1 

    return reporte

def mostrar_batacazos(archivo_1, archivo_2):
    partidos = lectura_archivo(archivo_1)
    ranking = lectura_archivo(archivo_2)
    if partidos is None or ranking is None:
        return
    year = input("Ingrese un año: ")
    valido = False
    while not valido:
        res = validacion_anio(year, archivo_1)
        if res == "A":
            print("Año incorrecto.")
            year = input("Ingrese un año: ")
        elif res == "B":
            print("En ese año no se jugó el Mundial.")
            year = input("Ingrese un año: ")
        else:
            if res == "C":
                valido = True
    
    partidos_total = filtro(partidos, [0,1,7,6])
    for line in partidos_total:
        line[3] = extraccion_anio(line[3])
    
    reporte = ""
    for line in partidos_total:
        if line[3] == int(year):
                score = resultado_partido(line,2)
                top_local = posicion_rankinkg(score[0], archivo_2)
                top_visitante = posicion_rankinkg(score[1], archivo_2)
                
                if top_local != None and top_visitante != None:
                    if int(score[2][0]) > int(score[2][1]):
                        if top_local > 10 and top_visitante <= 10:
                            reporte += f"{score[0]} (puesto {top_local}) venció a {score[1]} (puesto {top_visitante}). \n"
                    elif int(score[2][1]) > int(score[2][0]):
                        if top_local <= 10 and top_visitante > 10:
                            reporte += f"{score[1]} (puesto {top_visitante}) venció a {score[0]} (puesto {top_local}). \n"
    
    return reporte

def victorias_americanas(archivo_1, archivo_2):
    partidos = lectura_archivo(archivo_1)
    ranking = lectura_archivo(archivo_2)
    if partidos is None or ranking is None:
        return 
    
    partidos_total = filtro(partidos, [0,1,5,6,7])
    partidos_filtrados = filtro_fase_de_grupos(partidos_total)
    for line in partidos_filtrados:
        anio = extraccion_anio(line[3])
        mes = extraccion_mes(line[3])
        dia = extraccion_dia(line[3])
        line[3] = [anio, mes, dia]
        
    partidos_fechas_ordenadas = ordenar_fecha_des(partidos_filtrados, 3)
    reporte = ""
    for line in partidos_fechas_ordenadas:
        score = resultado_partido(line, 4)
        conf_local = confederacion(line[0], archivo_2)
        conf_visitante = confederacion(line[1], archivo_2)
        
        if conf_local != None and conf_visitante != None:
            if int(score[4][0]) > int(score[4][1]):
                if (conf_local == "CONMEBOL" or conf_local == "CONCACAF") and conf_visitante == "UEFA":
                    reporte += f"{score[0]} ({conf_local}) eliminó a {score[1]} ({conf_visitante}) el {line[3][0]}-{line[3][1]}-{line[3][2]}. \n"
            if int(score[4][1]) > int(score[4][0]):
                if (conf_visitante == "CONMEBOL" or conf_visitante == "CONCACAF") and conf_local == "UEFA":
                    reporte += f"{score[1]} ({conf_visitante}) eliminó a {score[0]} ({conf_local}) el {line[3][0]}-{line[3][1]}-{line[3][2]}. \n"
    return reporte

def grandes_leyendas(archivo_1, archivo_2):
    partidos = lectura_archivo(archivo_1)
    if partidos == None :
        return
    
    lista_filtrada = filtro(partidos, [0,1,2,3])
    lista_cap_pais = lista_capitanes_pais(lista_filtrada)
    for line in lista_cap_pais:
        partidos_jugados_cap = contador_partidos_por_capitan(line[0], archivo_1)
        line.append(partidos_jugados_cap)
   
    lista_cap_pais = ordenar_des(lista_cap_pais, 2) 

    cont = 1
    i = 0
    lista_pre_archivo = []
    while i < len(lista_cap_pais) - 1 and cont <= 5:
        lista_pre_archivo.append(lista_cap_pais[i])
        
        if i + 1 < len(lista_cap_pais):
            if lista_cap_pais[i][2] != lista_cap_pais[i+1][2]:
                cont += 1
        i +=1 
    
    archivo = ""
    for line in lista_pre_archivo:
        archivo += f"{line[0]} ({line[1]}) representó a su país como capitán {line[2]} veces.\n"
    
    crear_archivo("grandes_leyendas.txt", archivo)
        


def main():
    reporte1 = promedio_asistentes(archivo_1, archivo_2)
    print(reporte1)
    reporte2 = mostrar_batacazos(archivo_1, archivo_2)
    print(reporte2)
    reporte3 = victorias_americanas(archivo_1, archivo_2)
    print(reporte3)
    grandes_leyendas(archivo_1, archivo_2)
    
    return

main()

