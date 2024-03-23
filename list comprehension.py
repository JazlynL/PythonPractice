if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    listExample = []
    num = 0
    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):

                if a + b + c != n:
                    listExample.append([])
                    listExample[num] = [a, b, c]
                    num += 1

    print(listExample, end="")
