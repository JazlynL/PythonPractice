if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tups = []
for i in integer_list:
    tups.append(i)

print(hash(tuple(tups)))
