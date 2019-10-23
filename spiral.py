# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке

n = int(input())
a = [[0 for i in range(n)] for i in range(n)]
if n > 1:
    k = 0
    while n != 0:
        for i in range(k, n):
            for j in range(k, n):
                if i == k:
                    a[i][j] = a[i][j-1] + 1
                elif i != k and j == n-1:
                    a[i][j] = a[i-1][j] + 1
        for i in range(n-1, k-1, -1):
            for j in range(n-1, k-1, -1):
                if i == n-1 and j != n-1:
                    a[i][j] = a[i][j+1] + 1
                elif j == k and i != n-1 and i != k:
                    a[i][j] = a[i+1][j] + 1
        k += 1
        n -= 1
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end=' ')
        print()
else: print(n)