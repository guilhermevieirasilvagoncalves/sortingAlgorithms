/*
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 5th semester
*/

#include <iostream>

void selectionSort(int arr[], int n){

    int i, j, min;
    for (i = 0; i < n - 1; i++) {
        min = i;
        for (j = i+1; j < n; j++) if (arr[j] < arr[min]) min = j;
        int aux = arr[min];
        arr[min] = arr[i];
        arr[i] = aux;

    }

}

int main() {
    int arr[] = {10, 7, 3, 8, 4, 2, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;


}
