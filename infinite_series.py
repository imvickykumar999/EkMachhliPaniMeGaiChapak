
def check(s, t, c):
    p = input('\n>>> ')

    if p != '':
        try: 
            s.remove(int(p))
            t -= 1
            c -= 1
        except: 
            pass

    c += 1
    print(s)
    return s, t, c

def main():
    t = 6
    n, c = 0, 0
    s = list(range(1,t+1))

    while len(s) != 1:
        n += 1
        
        print('Player', s[c%t], ':', n, 'Machhli')
        s, t, c = check(s, t, c)

        for i in range(1, n+1):
            print('Player', s[c%t], ':', 'Pani me gai')
            s, t, c = check(s, t, c)

        for i in range(1, n+1):
            print('Player', s[c%t], ':', 'Chhapak')
            s, t, c = check(s, t, c)

    print('Winner :', s[0])

if __name__ == "__main__":
    main()
