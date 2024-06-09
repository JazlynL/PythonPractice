from collections import Counter

if __name__ == '__main__':
    dicttest = {}
    listtwo = []
    listname = []
    listAfter = []
    listsort = []
    counter = 0

    for _ in range(int(input())):
        name = input()
        score = float(input())
        listname.append(name)
        listtwo.append(score)

    # listname = [item for item in name.split()]
    # listScore = [item for item in str(score).split()]

dictTest = dict(zip(listname, listtwo))
listAfter = list(sorted(dictTest.items(), key=lambda kv: kv[1], reverse=False))[1:]

count_dict = Counter(dictTest.values())

for key, value in listAfter:
    counter += 1
    if counter == 1 and count_dict[value] == 1:
        print(key)
    elif count_dict[value] > 1 and counter <= 2:
        listsort.append(key)

for item in sorted(listsort):
    print(item)
