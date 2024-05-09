# Adilia Getia Haqia Ilmi
# 21120122120030

def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1.0

    for k in range(n):
        U[k][k] = A[k][k]
        for j in range(k+1, n):
            L[j][k] = A[j][k] / U[k][k]
            U[k][j] = A[k][j]
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] -= L[i][k] * U[k][j]

    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    return y

def backward_substitution(U, y):
    n = len(y)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def lu_gauss_solver(A, b):
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# Contoh Penggunaan
A = [[3, -1, 1],
     [-2, 2, 3],
     [1, 3, -2]]

b = [4, 11, 1]
# Menyelesaikan SPL
x = lu_gauss_solver(A, b)
print("Solusi SPL:", x)
