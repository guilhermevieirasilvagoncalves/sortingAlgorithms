'''
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 4th semester
    @algorithmComplexity: O(n+k)
'''

def countingSort(arr):
    size: int = max(arr) + 1 # descobre o tamanho do array de contagem
        
    countVet = [0] * size # cria o vetor de contagem

    for i in range(0,len(arr)):
        countVet[arr[i]] += int(1) # coloca a quantidade de vezes que cada numero se repete em seu index
    

    for j in range(1, len(countVet)):
        countVet[j] += countVet[j-1] # soma o index posterior com o anterior


    ordVet = [0] * len(arr) # cria o vetor onde será armazenado os numeros ordenados

    for t in range(len(arr)-1, -1, -1):
        ordVet[countVet[arr[t]]-1] = arr[t] # pega o valor do arr, o index deste valor no countVet
        countVet[arr[t]] -= 1               # o valor que está dentro deste index o countVet é usado
        #subtrai o valor do countVet        # como index no ordVet

    return ordVet # retorna um valor ordenado

def main():
    arr = [1,4,1,2,7,5,2]
    arrOrd = countingSort(arr)
    print(arrOrd)

if __name__ == "__main__":
    main()

