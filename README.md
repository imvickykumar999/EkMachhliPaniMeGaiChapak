# `Ek Machhli Pani Me Gai Chapak`

    Formula to continue series up to infinite.

```python
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
```

    Let total players, t = 6
        
```text
Player 1 : 1 Machhli
Player 2 : Pani me gai
Player 3 : Chhapak

Player 4 : 2 Machhli
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Chhapak
Player 2 : Chhapak

Player 3 : 3 Machhli
Player 4 : Pani me gai
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Chhapak
Player 2 : Chhapak
Player 3 : Chhapak

Player 4 : 4 Machhli
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Pani me gai
Player 2 : Pani me gai
Player 3 : Chhapak
Player 4 : Chhapak
Player 5 : Chhapak
Player 6 : Chhapak

Player 1 : 5 Machhli
Player 2 : Pani me gai
Player 3 : Pani me gai
Player 4 : Pani me gai
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Chhapak
Player 2 : Chhapak
Player 3 : Chhapak
Player 4 : Chhapak
Player 5 : Chhapak

Player 6 : 6 Machhli
Player 1 : Pani me gai
Player 2 : Pani me gai
Player 3 : Pani me gai
Player 4 : Pani me gai
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Chhapak
Player 2 : Chhapak
Player 3 : Chhapak
Player 4 : Chhapak
Player 5 : Chhapak
Player 6 : Chhapak

Player 1 : 7 Machhli
Player 2 : Pani me gai
Player 3 : Pani me gai
Player 4 : Pani me gai
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Pani me gai
Player 2 : Pani me gai
Player 3 : Chhapak
Player 4 : Chhapak
Player 5 : Chhapak
Player 6 : Chhapak
Player 1 : Chhapak
Player 2 : Chhapak
Player 3 : Chhapak

Player 4 : 8 Machhli
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Pani me gai
Player 2 : Pani me gai
Player 3 : Pani me gai
Player 4 : Pani me gai
Player 5 : Pani me gai
Player 6 : Pani me gai
Player 1 : Chhapak
Player 2 : Chhapak
Player 3 : Chhapak
Player 4 : Chhapak
Player 5 : Chhapak
Player 6 : Chhapak
Player 1 : Chhapak
Player 2 : Chhapak

... and so on.
```
