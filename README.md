# `Ek Machhli Pani Me Gai Chapak`

    Formula to continue series up to infinite.

```python
n = 0
while True:
    n += 1
    
    print(n, 'Machhli')

    for i in range(1, n+1):
        print('Pani me gai')

    for i in range(1, n+1):
        print('Chhapak')
        
    input()
```

```text
1 Machhli
Pani me gai
Chhapak

2 Machhli
Pani me gai
Pani me gai
Chhapak
Chhapak

3 Machhli
Pani me gai
Pani me gai
Pani me gai
Chhapak
Chhapak
Chhapak

4 Machhli
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Chhapak
Chhapak
Chhapak
Chhapak

5 Machhli
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Chhapak
Chhapak
Chhapak
Chhapak
Chhapak

6 Machhli
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Chhapak
Chhapak
Chhapak
Chhapak
Chhapak
Chhapak

7 Machhli
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Pani me gai
Chhapak
Chhapak
Chhapak
Chhapak
Chhapak
Chhapak
Chhapak

... and so on.
```
