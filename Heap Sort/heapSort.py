'''
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 4th semester
    @algorithmComplexity: O(n log(n))
'''
from typing import List

def fe(x: int):
    return 2*x+1

def fd(x: int):
    return 2*x+2

def pai(x: int):
    return (x-1)/2

def ultimoPai(n: int):
    return pai(n - 1)

def sift(idx: int, n: int, v: List[int]):
    
    if idx > ultimoPai(n):
        return False
    
    idxMax: int = fe(idx)

    if(fd(idx) < n and v[fd(idx)] > v[idxMax]):
        idxMax = fd(idx)

    if v[idxMax] > v[idx]:
        v[idxMax], v[idx] = v[idx] , v[idxMax]
        sift(idxMax, n, v)

def heapSort(arr):
    N = len(arr)

    for j in range(N-1 , -1, -1):
        sift(j, len(arr), arr)
    
    tam=len(arr)
    for i in range(0,N-1):
        arr[0], arr[tam-1] = arr[tam-1], arr[0]
        tam-=1
        c: int = int(ultimoPai(tam))
        while(c != 0):
            sift(c, tam, arr)
            c = int(pai(c))
        sift(0,tam, arr)
    
    return arr

def main():
    arr = [12, 11, 13, 5, 6, 7]
    arrOrd = heapSort(arr)
    print(arrOrd)

if __name__ == '__main__':
    main()
