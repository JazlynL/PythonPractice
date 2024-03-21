if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    listofarr = list(arr)
    result = [a for a in listofarr if a < max(listofarr)]

    print(max(result))


