# 📐 Resolução de Sistemas Lineares — Gauss, LU, Jacobi e Gauss-Seidel

Exemplo didático em Python para resolver sistemas lineares Ax = b, com métodos **diretos** e **iterativos**, comentados passo a passo.

---

## 🔹 Visão Geral

Este repositório apresenta implementações para resolver sistemas lineares usando:

| Tipo        | Métodos                         |
|------------|--------------------------------|
| Direto     | Gauss, LU                      |
| Iterativo  | Jacobi, Gauss–Seidel           |

Objetivo: ensinar de forma clara como cada método funciona.

---

## 🔹 Matemática

**Problema:** Resolver

A x = b

markdown
Copiar código

onde `A` é uma matriz n x n e `b` é um vetor de tamanho n.

### 1️⃣ Eliminação de Gauss

- Transformar A em **triangular superior** U  
- Resolver U x = b' por **retrossubstituição**  

**Exemplo de cálculo:**

x_n = b_n / U_nn
x_i = (b_i - sum_{j=i+1}^{n} U_ij * x_j) / U_ii

yaml
Copiar código

---

### 2️⃣ Fatoração LU

A = L * U

yaml
Copiar código

- L = triangular inferior com diagonal 1  
- U = triangular superior  
- Resolver L y = b  
- Resolver U x = y  

**Resumo:**

| Passo | Operação |
|-------|----------|
| 1     | Encontrar L e U |
| 2     | L y = b (substituição direta) |
| 3     | U x = y (retrossubstituição) |

---

### 3️⃣ Jacobi (Iterativo)

- Decomposição: A = D + R, onde D = diagonal  
- Iteração:

x_i^(k+1) = (b_i - sum_{j!=i} A_ij * x_j^(k)) / A_ii

yaml
Copiar código

- Cada iteração usa **valores da iteração anterior**  

---

### 4️⃣ Gauss-Seidel (Iterativo)

- Atualiza cada componente **imediatamente**:

x_i^(k+1) = (b_i - sum_{j<i} A_ij * x_j^(k+1) - sum_{j>i} A_ij * x_j^(k)) / A_ii

yaml
Copiar código

- Convergência mais rápida que Jacobi em geral  

---

## 🔹 Complexidade

| Método             | Custo Assintótico | Observação                               |
|------------------|-----------------|-----------------------------------------|
| Gauss / LU        | O(n^3)          | Fatoração + resolução de subsistemas O(n^2) |
| Jacobi / Gauss–Seidel | O(n^2) por iteração | Convergência depende da matriz (ex.: diagonal dominante) |

---

## 🔹 Exemplo em Python

```python
# Matriz de exemplo
a = [
  [5, 2, 1],
  [-1, 4, 2],
  [2, -3, 10]
]
b = [-12, 20, 3]

# ---- Método LU ----
L, U, x = lu(a, b)
print("Matriz L:", L)
print("Matriz U:", U)
print("Solução (LU):", x)

# ---- Gauss ----
x_gauss = gauss(a, b)
print("Solução (Gauss):", x_gauss)

# ---- Gauss-Seidel ----
x_gs = gauss_seidel(a, b, chute_inicial=[0,0,0])
print("Solução (Gauss-Seidel):", x_gs)
