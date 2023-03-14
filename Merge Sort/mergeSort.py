'''
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 5th semester
'''

def merge(v, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    E = [0] * (n1 + 1)
    D = [0] * (n2 + 1)
    for i in range(n1):
        E[i] = v[p + i]
    for j in range(n2):
        D[j] = v[q + j + 1]

    E[n1] = float('inf')
    D[n2] = float('inf')
    i = j = 0
    for k in range(p, r + 1):
        if E[i] <= D[j]:
            v[k] = E[i]
            i += 1
        else:
            v[k] = D[j]
            j += 1


def mergeSort(v, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(v, p, q)
        mergeSort(v, q + 1, r)
        merge(v, p, q, r)

def main():
    arr = [10, 7, 3, 8, 4, 2, 5]
    n = len(arr)
    mergeSort(arr, 0, n - 1)
    print("Array ordenado: ", end="")
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    main()
