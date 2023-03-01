'''
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 5th semester
'''

def bubblesort(v):
    for i in range(len(v) - 1):
        for j in range(len(v) - 1, i, -1):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]           
    return v

def main():
    v = [1, 5, 3, 4, 2]
    print(v)
    v = bubblesort(v)
    print(v)
    
if __name__ == "__main__":
    main()
