if __name__ == '__main__':
    listOne = []
    N = int(input())
for test in range(N):
    arr = input().split()
    match arr[0]:
        case 'insert'
            #insert method
            listOne.insert(int(arr[1]), int(arr[2]))
        case 'print':
            print(listOne)
        case 'remove':
            #remove method
            listOne.remove(int(arr[1]))

        case 'append':
            #append method
            listOne.append(int(arr[1]))

        case 'sort':
            #sort method
            listOne.sort()
        case 'pop':
            #pop method
            listOne.pop()
        case 'reverse':
            #reverse method
            listOne.reverse()