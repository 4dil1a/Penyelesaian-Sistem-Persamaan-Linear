# Adilia Getia Haqia Ilmi
# 21120122120030

# Fungsi untuk mencari transpose dari sebuah matriks
def transpose(matriks):
    return [[matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))]

# Fungsi untuk mencari determinan dari sebuah matriks
def determinan(matriks):
    n = len(matriks)
    if n == 1:
        return matriks[0][0]
    elif n == 2:
        return matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0]
    else:
        det = 0
        for i in range(n):
            sub_matriks = [baris[:i] + baris[i+1:] for baris in matriks[1:]]
            det += (-1) ** i * matriks[0][i] * determinan(sub_matriks)
        return det

# Fungsi untuk mencari invers dari sebuah matriks
def invers(matriks):
    n = len(matriks)
    if n == 1:
        return [[1 / matriks[0][0]]]
    elif n == 2:
        det = determinan(matriks)
        if det == 0:
            return None  # Matriks singular, invers tidak ada
        else:
            inv_det = 1 / det
            return [[matriks[1][1] * inv_det, -matriks[0][1] * inv_det],
                    [-matriks[1][0] * inv_det, matriks[0][0] * inv_det]]
    else:
        det = determinan(matriks)
        if det == 0:
            return None  # Matriks singular, invers tidak ada
        else:
            kofaktor = []
            for i in range(n):
                baris = []
                for j in range(n):
                    sub_matriks = [baris[:j] + baris[j+1:] for baris in (matriks[:i] + matriks[i+1:])]
                    kofaktor_elemen = (-1) ** (i + j) * determinan(sub_matriks)
                    baris.append(kofaktor_elemen)
                kofaktor.append(baris)
            adjoin = transpose(kofaktor)
            inv_det = 1 / det
            return [[elemen * inv_det for elemen in baris] for baris in adjoin]

# Fungsi untuk mengalikan dua matriks
def kali_matriks(matriks1, matriks2):
    return [[sum(matriks1[i][k] * matriks2[k][j] for k in range(len(matriks2))) 
             for j in range(len(matriks2[0]))] for i in range(len(matriks1))]

# Fungsi untuk menyelesaikan sistem persamaan linear menggunakan metode matriks invers
def selesaikan_sistem_linear(A, b):
    if len(A) != len(A[0]) or len(A) != len(b):
        return None  # Dimensi tidak cocok
    else:
        A_inv = invers(A)
        if A_inv is None:
            return None  # Matriks singular, invers tidak ada
        
        # Hitung vektor solusi x
        return kali_matriks(A_inv, transpose([b]))

# Contoh penggunaan
A = [[3, -1, 1],
     [-2, 2, 3],
     [1, 3, -2]]

b = [4, 11, 1]
solusi = selesaikan_sistem_linear(A, b)
if solusi is not None:
    print("Solusi SPL:", solusi)
else:
    print("Matriks koefisien A adalah singular, invers tidak ada.")