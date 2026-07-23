import csv

#Funcion para leer archivos, 
def lectura_archivo(nombre_archivo):
    res = []
    try:
        with open(nombre_archivo, 'r', encoding= "utf-8") as archivo:
            lector = csv.reader(archivo)
            for line in lector:
                res.append(line)
        return res[1:]
    except FileNotFoundError:
        print("No se encontró el archivo solicitado.")
        return None

#funcion para extraer el año del partido
def extraccion_anio(n):
    i = 0
    espacio = " "
    while n[i] == espacio:
        i += 1
    res = int(n[i:i+4])
    return res

#funcion para extraer mes del partido
def extraccion_mes(n):
    i = 0
    espacio = " "
    while n[i] == espacio:
        i += 1
    res = int(n[i+5:i+7])
    return res

#funcion para extraer dia del partido
def extraccion_dia(n):
    i = 0
    espacio = " "
    while n[i] == espacio:
        i += 1
    res = int(n[i+8:i+10])
    return res

#funcion para ordenar de menor a mayor los años de mundiales
def ordenar_as(lista, col):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j][col] > lista[j+1][col]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return lista
        
        
#funcion extraer y ordenar (preparacion datos para funcion 1)
def extraer_ordenar(nombre_archivo):
    n = lectura_archivo(nombre_archivo)
    if n == None:
        return
    
    lista_reducida = []
    for line in n:
        lista_reducida.append([extraccion_anio(line[6]), int(line[4])])
    
    lista_reducida = ordenar_as(lista_reducida, 0)
    return lista_reducida

# funcion para crear archivos de texto
def crear_archivo(arch, escritura):
    with open(arch, "w") as archivo_nuevo:
        archivo_nuevo.write(escritura)
        

##################################

def filtro(datos, columna):
    res = []
    for line in datos:
        if max(columna) < len(line):
            h =[]
            for i in columna:
                h.append(line[i])
            res.append(h)
    return res
    
def validacion_anio(year, archivo_1):
    try:
        year =int(year)
    except Exception:
        return "A"
    
    if year <= 0:
        return "A"
    else:
        partidos = lectura_archivo(archivo_1)
        fechas_mundiales = filtro(partidos, [6])
        anios_mundiales = []
        for i in fechas_mundiales:
            if i and i[0]:
                anio = extraccion_anio(i[0])
                if anio not in anios_mundiales:
                    anios_mundiales.append(anio)
        
        if year not in anios_mundiales:
            return "B" 
        else:
            return "C"
    
def extraccion_espacios(n):
    i = 0
    res = ""
    while i < len(n):
        if n[i] != " ":
            res += n[i]
        i += 1
    return res
        

def resultado_partido(partido, col):
    resultado = partido[col]
    resultado = extraccion_espacios(resultado)
    i = 0
    penales = False
    while i < len(resultado) and penales == False:
        if resultado[i] == "(" or resultado[i] == ")":
            penales = True
        i += 1
    
    local = ""
    visitante = ""
    if penales:
        i = 0
        contador_p1 = 0
        contador_p2 = 0
        while i < len(resultado):
            if resultado[i] == "(":
                contador_p1 += 1
            if resultado[i] == ")":
                contador_p2 += 1
            
            if contador_p1 == 1 and contador_p2 == 0 and "0" <= resultado[i] <= "9":
                local += resultado[i]
            if contador_p1 == 2 and contador_p2 == 1 and "0" <= resultado[i] <= "9":
                visitante += resultado[i]
            i += 1
    else:
        cont_guion = 0
        i = 0
        while i < len(resultado):
            if resultado[i] == "-":
                cont_guion += 1
            
            if cont_guion == 0 and "0" <= resultado[i] <= "9":
                local += resultado[i]
            if cont_guion == 1 and "0" <= resultado[i] <= "9":
                visitante += resultado[i]
            i += 1
    
    local = int(local)
    visitante = int(visitante)
    score = [local, visitante]
    partido[col] = score
    return partido
    
#podemos asumir que todos los paises estan igual escritos en ambas bases de datos
def posicion_rankinkg(pais, archivo_2):
    ranking = lectura_archivo(archivo_2)
    paises_in_ranking =[]
    for line in ranking:
        paises_in_ranking.append(line[0])
    for line in ranking:
        if pais not in paises_in_ranking:
            return None
        if line[0]==pais:
            return int(line[3])
       
    
#################################################

def convert_minus(s):
    res = ""
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in s:
        if c in mayus:
            res += chr(ord(c)+32)
        else:
            res += c
    
    return res
    

def filtro_fase_de_grupos(x):
    filtrada = []
    fases_de_grupo = ["groupstage", "secondgroupstage", "firstgroupstage", "secondround", "firstround", "groupstageplay-off"]
    for line in x:
        line[2] = extraccion_espacios(line[2])
        line[2] = convert_minus(line[2])
        if line[2] not in fases_de_grupo:
            filtrada.append(line)
    
    return filtrada
        
        
def ordenar_fecha_des(lista, col):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j][col][0] < lista[j+1][col][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            
            elif lista[j][col][0] == lista[j+1][col][0]:
                if lista[j][col][1] < lista[j+1][col][1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    
                elif lista[j][col][1] == lista[j+1][col][1]:
                    if lista[j][col][2] < lista[j+1][col][2]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

def confederacion(pais, archivo_2):
    pais = extraccion_espacios(pais)
    pais = convert_minus(pais)
    ranking = lectura_archivo(archivo_2)
    if ranking == None:
        return
    for line in ranking:
        line[0] = extraccion_espacios(line[0])
        line[0] = convert_minus(line[0])
        if line[0] == pais:
            return line[2]
        
        
##############################################


def lista_capitanes_pais(x):
    capitanes_pais  =[]
    capitanes_vistos = []
    
    for line in x:
        cap_local = extraccion_espacios(line[2])
        cap_visitante = extraccion_espacios(line[3])
        
        if cap_local not in capitanes_vistos and cap_local != "":
            capitanes_pais.append([cap_local, line[0]])
            capitanes_vistos.append(cap_local)
            
        if cap_visitante not in capitanes_vistos and cap_visitante != "":
            capitanes_pais.append([cap_visitante, line[1]])
            capitanes_vistos.append(cap_visitante)
    
    return capitanes_pais
                                
def contador_partidos_por_capitan(capitan, archivo_1):
    partidos = lectura_archivo(archivo_1)
    if partidos == None :
        return
    
    capitan = extraccion_espacios(capitan)
    capitan = convert_minus(capitan)
    lista_filtrada = filtro(partidos, [2,3])
    cont_cap = 0
    for line in lista_filtrada:
        cap1 = convert_minus(extraccion_espacios(line[0]))
        cap2 = convert_minus(extraccion_espacios(line[1]))
        if cap1 == capitan or cap2 == capitan:
            cont_cap += 1
    
    return cont_cap
            
def ordenar_des(lista, col):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j][col] < lista[j+1][col]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return lista


               
      
    
    
    


            
        
        
    
    
    

    
    
    
    
    

        
        
        

        


                



                






        
        
            
        

        