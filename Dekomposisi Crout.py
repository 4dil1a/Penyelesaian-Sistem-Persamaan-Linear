# Adilia Getia Haqia Ilmi
# 21120122120030

def crout_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for j in range(n):
        U[j][j] = 1

        for i in range(j, n):
            sum_val = sum(L[i][k] * U[k][j] for k in range(i))
            L[i][j] = A[i][j] - sum_val

        for i in range(j, n):
            if L[j][j] == 0:
                return None, None  # Pivot 0, dekomposisi gagal
            sum_val = sum(L[j][k] * U[k][i] for k in range(j))
            U[j][i] = (A[j][i] - sum_val) / L[j][j]

    return L, U

def solve_crout(A, b):
    L, U = crout_decomposition(A)
    n = len(A)
    y = [0.0] * n
    x = [0.0] * n

    # Solve Ly = b
    for i in range(n):
        y[i] = (b[i] - sum(L[i][k] * y[k] for k in range(i))) / L[i][i]

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return x

# Contoh Penggunaan
A = [[3, -1, 1],
     [-2, 2, 3],
     [1, 3, -2]]

b = [4, 11, 1]

solution = solve_crout(A, b)
print("Solution:", solution)
