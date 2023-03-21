'''
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 5th semester
'''

def selectionSort(arr):
    n = len(arr)
    
    for i in range(0, n - 1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


def main():
    arr = [3,2,1,6]
    print(selectionSort(arr))

if __name__ == "__main__":
    main()
