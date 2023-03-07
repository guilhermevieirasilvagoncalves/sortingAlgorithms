#include <stdio.h>

int partition(int v[], int p, int r){
    int x = v[r];
    int i = p - 1;
    for(int j = p; j <= r - 1; j++){
        if(v[j] <= x){
            i++;
            int temp = v[i];
            v[i] = v[j];
            v[j] = temp;
        }
    }
    int temp = v[i + 1];
    v[i + 1] = v[r];
    v[r] = temp;
    return i + 1;
}

void quicksort(int v[], int p, int r){
    if(p < r){
        int q = partition(v, p, r);
        quicksort(v, p, q - 1);
        quicksort(v, q + 1, r);
    }
}

int main() {
    int arr[] = { 10, 7, 8, 9, 1, 5 };
    int n = sizeof(arr)/sizeof(arr[0]);
    quicksort(arr, 0, n - 1);
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}
