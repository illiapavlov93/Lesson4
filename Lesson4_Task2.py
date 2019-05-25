def multiplysum(a):
    b, d = [], []
    sumk = 0
    prelast = a[-2]
    for i in a:
        b.append(bin(i))
    for i in b:
        c = 0
        for x in i:
            if x == '1':
                c += 1
                if c % 2 == 0:
                    d.append(b.index(i))
    for i in a:
        if i in d:
            sumk += a[i]
    return sumk * prelast


a = [1, 2, 3, 4, 5]
print(multiplysum(a))
