'''
    @author: Guilherme Vieira Silva Gonçalves
    @course: Ciência da Computação, 5th semester
'''

def insertionsort(v):
    for j in range(0, len(v)):
        chave = v[j]
        i = j - 1
        while(i >= 0 and v[i] > chave):
            v[i + 1] = v[i]
            i = i - 1
        v[i + 1] = chave
    return v
        
def main():
    v = [3,2,1,6]
    print(insertionsort(v))

if __name__ == "__main__":
    main()
            
