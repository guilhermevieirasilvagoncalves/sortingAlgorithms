def quicksort(v,p,r):
    if p < r:
        q = partition(v,p,r)
        quicksort(v,p,q - 1)
        quicksort(v,q + 1, r)
    return v
        
def partition(v,p,r):
    x = v[r]
    i = p - 1
    for j in range(p, r):
        if v[j] <= x:
            i = i + 1
            v[i], v[j] = v[j], v[i]
    v[i + 1], v[r] = v[r], v[i + 1]
    return i + 1

def main():
    v = [6,2,5,1,4,3]
    print(quicksort(v, 0 , len(v) - 1))

if __name__ == "__main__":
    main()

