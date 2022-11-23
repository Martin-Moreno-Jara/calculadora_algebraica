import numpy as np

def sumar_matrices(matriz_A,Matriz_B):
    try:
        suma = matriz_A+Matriz_B
        return suma
    except:
        error ="No es posible la suma de estas matrices"
        return error
        
         

def crear_matriz(filas,columnas):
    f= -1
    c=-1
    e_fil = []
    for i in range(0,filas):
        e_col = []
        f+=1
        for j in range(0,columnas):
            c+=1
            valor=int(input(f"Ingrese el valor del componente {i+1},{j+1}: "))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil

matriz1 = np.array([[1,3],[2,4],[1,3]],float)
matriz2 = np.array([[1,1,2],[6,4,7],[1,2,8]],float)

print(sumar_matrices(matriz1,matriz2))


# print("\nPrimera matriz\n")
# matrizA = np.array(crear_matriz(3,3))

# print("\nSegunda matriz\n")
# matrizB = np.array(crear_matriz(3,3))

vectorA = np.array([1,2],float)
vectorB = np.array([4,5],float)

# suma = matrizA+matrizB
# resta = matrizA-matrizB
# multiplicacion = matrizA*matrizB
producto_punto = np.dot(vectorA,vectorB)

# print("suma\n",suma)
# print("resta\n",resta)
# print("multiplicación\n",multiplicacion)
# print(producto_punto)