# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def buddy(start, limit):
    a = []
    b = []
    c = []
    d = []
    for x in range(1, int(start**0.5)+1) :
        if start % x==0:
            a.append(x)
    for y in a:
        if start/y != 0:
            b.append(int(start/y))
    a.extend(b)
    a1 = list(set(a))
    a1.sort()
    for z in range(1, int(limit**0.5)+1) :
        if limit % z==0:
            c.append(z)
    for q in c:
        if limit/q != 0:
            d.append(int(limit/q))
    c.extend(d)
    c1 = list(set(c))
    c1.sort()
    n = sum(a1[:-1])-1
    m = sum(c1[:-1])-1


    if n >0 and n == limit and m >0 and m == start:
        if start <= n <= limit and m >n:
            return (n, m)
        else:
            return 'Nothing'
    else:
        return 'Nothing'

if __name__ == '__main__':
    print(buddy(48, 75))


