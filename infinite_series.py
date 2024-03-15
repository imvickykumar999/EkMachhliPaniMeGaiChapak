# main.py

def main():
    n = 0
    t = 6
    c = 0

    while True:
        n += 1
        
        print('Player', c%t +1, ':', n, 'Machhli')
        c += 1

        for i in range(1, n+1):
            print('Player', c%t +1, ':', 'Pani me gai')
            c += 1

        for i in range(1, n+1):
            print('Player', c%t +1, ':', 'Chhapak')
            c += 1
            
        input()

if __name__ == "__main__":
    main()
