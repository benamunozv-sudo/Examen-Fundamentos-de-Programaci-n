bodega = {'FLO1': [15990, 8], 'FLO2': [29990, 3], 'FLO3': [9990, 12]}
arreglos = {'FLO1': {'nombre': 'Ramo Primavera', 'tipo': 'ramo'}, 'FLO2': {'nombre': 'Arreglo Especial', 'tipo': 'ramo'}, 'FLO3': {'nombre': 'Base Flores', 'tipo': 'caja'}}

def leer_opcion():
    try: return int(input("Ingrese opción: "))
    except ValueError: return -1

def unidades_tipo(tipo):
    
    total = sum(bodega[c][1] for c in arreglos if arreglos[c]['tipo'].lower() == tipo.lower())
    print(f"El total de unidades disponibles es: {total}")

def buscar_codigo(codigo):
   
    return next((c for c in bodega if c.lower() == codigo.lower()), None)

def actualizar_precio(codigo, nuevo_precio):
    c = buscar_codigo(codigo)
    if c: bodega[c][0] = nuevo_precio; return True
    return False

def eliminar_arreglo(codigo):
    c = buscar_codigo(codigo)
    if c: del bodega[c], arreglos[c]; return True
    return False

def v_codigo(val): return len(val.strip()) > 0 and not buscar_codigo(val)
def v_nombre(val): return len(val.strip()) > 0
def v_tipo(val): return len(val.strip()) > 0
def v_color(val): return len(val.strip()) > 0
def v_tamano(val): return val.upper() in ['S', 'M', 'L']
def v_tarjeta(val): return val.lower() in ['s', 'n']
def v_temporada(val): return len(val.strip()) > 0
def v_precio(val): return val > 0
def v_unidades(val): return val >= 0

def agregar_arreglo(c, n, t, cp, tam, tar, temp, pre, uni):
   
    if v_codigo(c):
        bodega[c] = [pre, uni]
        arreglos[c] = {'nombre': n, 'tipo': t, 'color': cp, 'tamano': tam, 'tarjeta': tar.lower() == 's', 'temporada': temp}
        return True
    return False
