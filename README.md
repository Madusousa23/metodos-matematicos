# 📐 Resolução de Sistemas Lineares — Gauss, LU, Jacobi e Gauss–Seidel

Exemplo didático em Python para resolver sistemas lineares \(A x = b\), com implementações **diretas** e **iterativas**, explicado passo a passo.

---

## 🔹 Visão Geral

Este repositório contém implementações para resolver sistemas lineares usando métodos:

| Tipo        | Métodos                         |
|------------|--------------------------------|
| Direto     | Gauss, LU                      |
| Iterativo  | Jacobi, Gauss–Seidel           |

Objetivo: **ensinar o passo a passo** de cada técnica de forma clara e comentada.

---

## 🔹 Matemática

**Problema:** Resolver

\[
A x = b, \quad A \in \mathbb{R}^{n \times n},\ b \in \mathbb{R}^n
\]

### 1️⃣ Eliminação de Gauss

- Transformar \(A\) em **triangular superior** \(U\) por operações elementares.
- Resolver \(U x = \tilde{b}\) por retrossubstituição.

### 2️⃣ Fatoração LU

\[
A = L U
\]

- \(L\) = triangular inferior com diagonal unitária
- \(U\) = triangular superior  
- Resolver \(L y = b\) por substituição direta
- Resolver \(U x = y\) por retrossubstituição

### 3️⃣ Jacobi (Iterativo)

- Decomposição: \(A = D + R\), \(D\) = diagonal  
- Iteração:

\[
x^{(k+1)} = D^{-1} (b - R x^{(k)})
\]

### 4️⃣ Gauss–Seidel (Iterativo)

- Atualiza cada componente imediatamente:

\[
x_i^{(k+1)} = \frac{1}{a_{ii}}\Bigg(b_i - \sum_{j<i} a_{ij} x_j^{(k+1)} - \sum_{j>i} a_{ij} x_j^{(k)}\Bigg)
\]

---

## 🔹 Complexidade e Observações

| Método             | Custo Assintótico | Observação                              |
|------------------|-----------------|----------------------------------------|
| Gauss / LU        | \(O(n^3)\)       | Fatoração + solução de subsistemas \(O(n^2)\) |
| Jacobi / Gauss–Seidel | \(O(n^2)\)/iteração | Convergência depende da matriz (ex.: diagonal dominante) |

> Para sistemas grandes e esparsos, prefira bibliotecas especializadas (SciPy, PETSc).

---

## 🔹 Exemplo de Uso em Python

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
print("Solução:", x)

# ---- Gauss ----
x_gauss = gauss(a, b)
print("Solução (Gauss):", x_gauss)

# ---- Gauss-Seidel ----
x_gs = gauss_seidel(a, b, chute_inicial=[0,0,0])
print("Solução (Gauss-Seidel):", x_gs)
