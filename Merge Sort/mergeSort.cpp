#include <iostream>
#include <climits>

void merge(int v[], int p, int q, int r){
    int n1 = q - p + 1;
    int n2 = r - q;
    int E[n1 + 1];
    int D[n2 + 1];
    for (int i = 0; i < n1; i++) {
        E[i] = v[p + i];

    }
    for (int j = 0; j < n2; j++) {
        D[j] = v[q + j + 1];
    }
    E[n1] = INT_MAX;
    D[n2] = INT_MAX;
    int i = 0;
    int j = 0;
    for (int k = p; k <= r; k++) {
        if (E[i] <= D[j]) {
            v[k] = E[i];
            i++;
        }
        else{
            v[k] = D[j];
            j++;
        }
    }

}

void mergeSort(int v[], int p, int r){
    if (p < r) {
        int q = (p + r)/2;
        mergeSort(v, p, q);
        mergeSort(v, q + 1, r);
        merge(v, p, q, r);
    }
}

int main() {
    int arr[] = {10, 7, 3, 8, 4, 2, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}
