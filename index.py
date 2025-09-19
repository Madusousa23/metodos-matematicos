#Código Maria Eduarda 
#------CÓDIGO--------------

#Recebe a matriz dos coeficientes 𝐴 (como a) e o vetor dos termos independentes 𝑏.
#Vai calcular L, U e a solução 𝑥 do sistema.
def lu(a, b):
    n = len(a)  # número de linhas

    #LU
    L = [[0]*n for _ in range(n)] 
    U = [[0]*n for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            U[i][j] = a[i][j]
        L[i][i] = 1               

    #Escalonamento
    for k in range(n-1):                  
        for i in range(k+1, n):           
            m = U[i][k]/U[k][k]           
            L[i][k] = m                   
            for j in range(k, n):
                U[i][j] = U[i][j] - m * U[k][j] 
            b[i] = b[i] - m * b[k]        

    #Retrossubstituição
    x = [0]*n 
    x[n-1] = b[n-1]/U[n-1][n-1]   
    for i in range(n-2,-1,-1):    
        soma = 0                  
        for j in range(i+1, n):   
            soma += U[i][j]*x[j]  
        x[i] = (b[i]-soma)/U[i][i]  
    return L, U, x

#MÉTODO DE GAUSS
def gauss(a, b):
    n = len(a)  
    A = [linha[:] for linha in a]  
    B = b[:]

    for k in range(n-1):                     
        for i in range(k+1, n):              
            m = A[i][k]/A[k][k]              
            for j in range(k, n):
                A[i][j] = A[i][j] - m*A[k][j] 
            B[i] = B[i] - m*B[k]              

    x = [0]*n
    x[n-1] = B[n-1]/A[n-1][n-1]              
    for i in range(n-2, -1, -1):             
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j]*x[j]
        x[i] = (B[i]-soma)/A[i][i]           
    return x


#GAUSS-SEIDEL
def gauss_seidel(a, b, chute_inicial=None, max_iter=100, tol=1e-6):
    n = len(a)
    x = [0]*n if chute_inicial is None else chute_inicial[:]  # chute inicial
    for iteracao in range(max_iter):
        x_novo = x[:]  # para armazenar os novos valores de x
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += a[i][j]*x_novo[j]  # já usa valores atualizados
            x_novo[i] = (b[i] - soma)/a[i][i]
        # critério de parada
        erro = max(abs(x_novo[k]-x[k]) for k in range(n))
        x = x_novo
        if erro < tol:
            break
    return x


#JACOBI
def jacobi(a, b, chute_inicial=None, max_iter=100, tol=1e-6):
    n = len(a)
    x = [0]*n if chute_inicial is None else chute_inicial[:]  # chute inicial
    for iteracao in range(max_iter):
        x_novo = [0]*n  # todos os valores novos são calculados com base na iteração anterior
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += a[i][j]*x[j]  # usa sempre valores da iteração anterior
            x_novo[i] = (b[i] - soma)/a[i][i]
        # critério de parada
        erro = max(abs(x_novo[k]-x[k]) for k in range(n))
        x = x_novo
        if erro < tol:
            break
    return x



a = [
  [5,2,1],
  [-1,4,2],
  [2,-3,10]
]
b1 = [-12, 20, 3]
b2 = [-12, 20, 3]
b3 = [-12, 20, 3]
b4 = [-12, 20, 3]

L, U, solucao_lu = lu(a, b1)

print("Matriz L:")
for linha in L:
    print(linha)

print("\nMatriz U:")
for linha in U:
    print(linha)

print("\nSolução do sistema (LU):")
print(solucao_lu)

solucao_gauss = gauss(a, b2)
print("\nSolução do sistema (Gauss):")
print(solucao_gauss)

solucao_gauss_seidel = gauss_seidel(a, b3, chute_inicial=[0,0,0])
print("\nSolução do sistema (Gauss-Seidel):")
print(solucao_gauss_seidel)

solucao_jacobi = jacobi(a, b4, chute_inicial=[0,0,0])
print("\nSolução do sistema (Jacobi):")
print(solucao_jacobi)
