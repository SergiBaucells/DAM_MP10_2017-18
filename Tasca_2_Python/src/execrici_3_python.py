
def aproxima_pi(n):
    i = 1
    for j in range(1, n):
        i = i * 4 * j ** 2 / (4 * j ** 2 - 1)
    i *= 2

n = int(input('Quants termes? '))
print(aproxima_pi(n))