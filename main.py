import validaciones as v

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por tipo de arreglo")
        print("2. Búsqueda de arreglos por rango de precio")
        print("3. Actualizar precio de arreglo")
        print("4. Agregar arreglo")
        print("5. Eliminar arreglo")
        print("6. Salir")
        print("=====================================")
        
        op = v.leer_opcion()
        
        if op == 1:
            v.unidades_tipo(input("Ingrese tipo de arreglo a consultar: "))
            
        elif op == 2:
            try:
                pmin, pmax = int(input("Precio mín: ")), int(input("Precio máx: "))
                res = [f"{v.arreglos[c]['nombre']} -- {c}" for c in v.bodega 
                       if pmin <= v.bodega[c][0] <= pmax and v.bodega[c][1] > 0]
                print(f"Encontrados: {sorted(res)}" if res else "No hay arreglos en ese rango.")
            except ValueError: print("Debe ingresar valores enteros")
            
        elif op == 3:
            while True:
                cod = input("Código del arreglo: ")
                try:
                    res = v.actualizar_precio(cod, int(input("Nuevo precio: ")))
                    print("Precio actualizado" if res else "El código no existe")
                except ValueError: print("Precio inválido")
                if input("¿Actualizar otro? (s/n): ").lower() != 's': break
                
        elif op == 4:
            c = input("Código: "); n = input("Nombre: "); t = input("Tipo: "); col = input("Color: ")
            tam = input("Tamaño (S/M/L): "); tar = input("Incluye tarjeta (s/n): "); temp = input("Temporada: ")
            try:
                pre, uni = int(input("Precio: ")), int(input("Unidades: "))
                valid = all([v.v_codigo(c), v.v_nombre(n), v.v_tipo(t), v.v_color(col), v.v_tamano(tam), 
                             v.v_tarjeta(tar), v.v_temporada(temp), v.v_precio(pre), v.v_unidades(uni)])
                if valid:
                    print("Arreglo agregado" if v.agregar_arreglo(c, n, t, col, tam, tar, temp, pre, uni) else "El código ya existe")
                else: print("Error en validación de datos")
            except ValueError: print("Datos numéricos inválidos")
            
        elif op == 5:
            cod = input("Código a eliminar: ")
            print("Arreglo eliminado" if v.eliminar_arreglo(cod) else "El código no existe")
            
        elif op == 6:
            print("Programa finalizado"); break
        else:
            print("Debe seleccionar una opción válida")

if __name__ == "__main__":
    main()
